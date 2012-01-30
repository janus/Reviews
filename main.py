from bottle import  route, request, get, post, static_file, template, redirect,debug
import MySQLdb
from model.model import  Users,Reviews, helper
from session import app_others, logged_in_user, add_url, new_app, user_session, success_message, error_message, add_token

#Could be removed ...the above made it redundant


def blogtime(my_date):
    year, month, day = map(int, my_date.split('-'))
    return datetime.date(year, month, day)

@app_others.get('/:filename#.+\.(css|js|ico|png|gif|jpg|jpeg|txt|html)#')
def static(filename):
    return static_file(filename, root='/home/rmicro/myPython/Reviews')

@app_others.route('/')
@app_others.route('/index')
def  index():
    try:

	token = add_token(helper.token)
	print token
	reviews =  Reviews.list_all_reviews()   
        return template("layout",  my_top=0, reviews = reviews, token = token )
    except MySQLdb.OperationalError ,e:
	redirect("/index")
    


@app_others.route('/json:json#[1-9]+#')
def show_json(json):
    return {'task': 'This item number does not exist!'}

@app_others.get('/login')
def login_form():
    try:
        user_details = logged_in_user()
	start_point = 1
	reviews =  Reviews.list_all_reviews() 
        if not user_details:
	    token = add_token(helper.token)
            return template("alogin", my_top=1, cond=0,token=token)
        else:
	    return template("layout",my_top=user_details["username"], reviews=reviews)
    except MySQLdb.OperationalError ,e:
	redirect("/index")

@app_others.post('/login')
def login_submit():
    email = request.forms.get('email').strip()
    password = request.forms.get('password').strip()
    obj_session = request.environ.get('beaker.session')
    token =  request.forms.get('form_token').strip()
    print "EMEKA"
    print token
    if token == obj_session["token"]:
	del obj_session["token"]
        try:
	    user =  Users.find_user_by_password_and_email(password, email)
	    if user:
	        user_session(user['id'])
	        s = request.environ.get('beaker.session')
	        if  s.has_key('url'):
	            url = s['url']
	            del s['url']	
	            redirect(url)	
		reviews =  Reviews.list_all_reviews()		    
	        return template("layout",my_top=user["username"], token=0, reviews=reviews)
	    else:
		print "OFFOR"
		return template("alogin", my_top=1, cond=1,token=token, error_message=error_message)  # template("failedlogin")
        except MySQLdb.OperationalError ,e:
	     return template("alogin", my_top=1, cond=1, token=token,error_message=error_message) # template("failedlogin")
    else:
	 return template("alogin", my_top=1, cond=1, token=token, error_message=error_message) 


@app_others.get('/logout')
def log_out():
    s = request.environ.get('beaker.session')
    del s['user_id'] 
    redirect('/index')


