from bottle import run, app, route, request, get, post, static_file, template, redirect,debug,validate
from beaker.middleware import SessionMiddleware
from mydatamodel import helper
import mymail
import MySQLdb
from mydatamodel import  model 


session_opts = {'session.type': 'file','session.cookie_expires': 300, 'session.data_dir': './data','session.auto': True }
my_app = SessionMiddleware(app(), session_opts)


	
def authenticate(handler):
  def _check_auth(*args,**kwargs):
    s = request.environ.get('beaker.session')
    if s['user_id']:
      user = model.Users.find_by_id(s['user_id'])
      if user:
        return handler(user, *args, **Kwargs)
        redirect('/alogin')
  return _check_auth
	
def logged_in_user():
  s = request.environ.get('beaker.session')
  if  s.has_key("user_id"):
      return model.Users.find_by_id(s['userid'])
  return None

def user_is_logged():
  if logged_in_user():
    return True
  return False
     # return {'foo': [{'moo': ('iop',56,233)}]}

def blogtime(my_date):
            year, month, day = map(int, my_date.split('-'))
            return datetime.date(year, month, day)
	    
def user_session(user_id):
	 s = request.environ.get('beaker.session')
	 s['user_id'] = user_id
	 s.save()

@get('/:filename#.+\.(css|js|ico|png|jpg|jpeg|txt|html)#')
def static(filename):
    return static_file(filename, root='/home/rmicro/myPython/myseunPython')

@route('/')
@route('/index.html/:my_test')
@route('/index')
def  index(my_test=None):
	return template("layout", title="Maamariga",  my_test=my_test)


@route('/json:json#[1-9]+#')
def show_json(json):
	return {'task': 'This item number does not exist!'}

@get('/alogin')
def login_form():
	       s = request.environ.get('beaker.session')
	       if not s.has_key('name') :
		          #s = request.environ.get('beaker.session')
                          return template("alogin",title="micolo", my_test=1)
	       else:
		       return "You are already login"


@get('/search')
def search():
	search  = request.GET.get('asearch')
	try:
		search_text = Reviews.search(search)
		if search_text:
			return template("search", rows=search_text)
	except MySQLdb.OperationalError, e:
			return template("search", rows = "<p>There is nothing there that matches your text</p>")


@get('/logout')
def log_out():
	s = request.environ.get('beaker.session')
	del s['user_id'] 
	redirect('/index')

@get('/review/:a/:b/:c/:name')
#@validated(a=int, b=int, c=int)
def get_review(a, b , c, name):
		created_time =  a.strip() + "-" + b.strip() + "-" + c.strip()
		try:
			review, comments = Reviews.get_url(created_time, name.strip())
			if review:
				return template("review", review = review, comments=comments)
			else:
				redirect('/index')
		except MySQLdb.OperationalError, e:
			redirect('/index')


@get('/review/:id')
@get('/review/:id/:name')
#@validate(id=int)
def get_review_id(id, name):
	try:
		review, comments = Reviews.get_by_id( id)
		if review:
			return template("review",  review = review, comments=comments)
		else:
			redirect('/index')
	except MySQLdb.OperationalError, e:
		redirect('/index')
		
@route('/Reviews/')
@route('/Reviews')
def get_all_Reviews():
	try:
		Reviews =  Reviews.list_all_Reviews()
		if Reviews:
			return template("list_Reviews", review = Reviews)
		else:
			redirect('/index')
	except MySQLdb.OperationalError, e:
		  redirect('/index')
		
		
@post('/review/edit')
@authenticate
def edit_review():
	title = request.forms.get('title').strip()
	entry = request.forms.get('entry').strip()
	review_id = request.forms.get('review_id').strip()
	s = request.environ.get('beaker.session')
	logged_id = s['user_id']
	if user_id == logged_id:
		try:
			status = Reviews.update(user_id,  review_id, entry, title)
			if status:
				link = "/review/%d/%s" %(review_id, "You just updated your review") 
				redirect(link)
			else:
				redirect('/index')
		except MySQLdb.OperationalError ,e:
			redirect('/index')
	else:
		redirect('/index')
			
	


#Todo be filtered morrow
@post('/review/create')
@authenticate
def create_review(user):
		title = request.forms.get('title').strip()
		entry = request.forms.get('entry').strip()
		logged_id = user['id']
		sector_id = request.forms.get('sector_id').strip()
		company_id = request.forms.get('company_id').strip()
		branch_id = request.forms.get('branch_id').strip()
		url = helper.get_url(title)
		try:
				review, comments =  model.Reviews.create(logged_id, sector_id, company_id, branch_id, title, entry,  url)
				if my_return:
				#my_return should be date in this form " 2011/10/7
					#my_link =  "/" + my_return + "/" + url
					#redirect( mylink)
					return  template("review",  review = review, comments=comments)
				else:
					redirect('/index')
		except MySQLdb.OperationalError , e:
			redirect('/index')

#Todo be filtered morrow
@post('/comment/create')
@authenticate
def create_comment(user, *args, **Kwargs):
		message = request.forms.get('message').strip()
		review_id = request.forms.get('review_id')
		s = request.environ.get('beaker.session')
		user_id = user['id']
		try:
				status =  model.Comments.create(user_id, review_id, message)
				review, comments = model.Reviews.get_by_id( review_id)
				if status:
					return template("review" , review = review, comments= comments)
				else:
					return template("review_error", message = "Failed to create your model.Comments", review = review, comments=comments)
		except MySQLdb.OperationalError , e:
				return template("review_error", message = "Failed to create your model.Comments", review = review, comments=comments)
				

@post('/review/edit')
@authenticate
def edit_comment(user, *args, **Kwargs):
	message = request.forms.get('message').strip()
	comment_id = request.forms.get('comment_id').strip()
	s = request.environ.get('beaker.session')
	logged_id = user['id']
	if user_id == logged_id:
		try:
			status = model.Comments.update(logged_id,  comment_id, message)
			if status:
				link = "/review/%d/%s" %(review_id, "You just updated your comment") 
				redirect(link)
			else:
				redirect('/index')
		except MySQLdb.OperationalError ,e:
			redirect('/index')
	else:
		redirect('/index')
			
@get('/activation')
def activate_account():
	print "OO"
	activation_number = request.GET.get('activate')
	print activation_number
	try:
		status = model.Users.activate(activation_number)
		if status: 
			return template("activation_message", message ="Your account is now activated" )
		else:
			redirect('/index')
	except MySQLdb.OperationalError , e:
		redirect('/index')
			


#Todo be filtered morrow
@post('/register')
def create_user():
	username = request.forms.get('username').strip()
	email       =  request.forms.get('email').strip()
	password =  request.forms.get('password').strip()
	conpassword = request.forms.get('conpassword').strip()
	activation_code = helper.activation_hash()
	if password == conpassword:
		try:
				if model.Users.create(username, email, activation_code, password):
					print "Send mail now"
					mymail.send_mail(username, email, activation_code)
					print "Mail sent"
					#return template("alogin",title="micolo", my_test=1)
					return template("registration", title="Maamariga", my_test=1, mysuccess = "Your account was successfully created",username=username, cond=1)
				else:
					return  template("failedregistration",title="Maamariga", my_test=1,error_message  = "You must have done something wrong", username=username)
		except MySQLdb.OperationalError ,e:
				return  template("failedregistration",title="Maamariga", my_test=1,error_message  = "You must have done something wrong", username=username)
	else:
		return  "Baader"
		


@post('/user/edit/password')
def update_password():
	password =  request.forms.get('password').strip()
	conpassword = request.forms.get('conpassword').strip()
	user_id = request.forms.get('user_id')
	if user_is_logged():
		if password == conpassword:
			try:
				my_return = model.Users.update_password(user_id, password)
				if my_return:
					mymail.send_mail(my_return['username'],  my_return['mail'])
					return template("registration",my_test = 1, mysuccess = "Your password updated successfully",  username=username , cond=2) 
			except MySQLdb.OperationalError , e:
				return  template("failedregistration", my_test =1, error_message  = "You must have done something wrong", username=username)


	
@post('/profile/create')
@authenticate
def create_profile(user, *args, **Kwargs):
	firstname = request.forms.get('firstname').strip()
	surname = request.forms.get('surname').strip()
	image = request.file.get('image')
	user_id = user['id']
	try:
			my_profile =  model.Profiles.create(firstname, surname, image, user_id)
			if my_profile:
				return template("profile", my_profile=my_profile)
	except MySQLdb.OperationalError , e:
			return  template("profile", profile_failed = "Something just went wrong")
	
@post('/profile/edit')
@authenticate
def edit_profile(user, *args, **Kwargs):
	firstname = request.forms.get('firstname').strip()
	surname = request.forms.get('surname').strip()
	image = request.file.get('image')  #To do
	user_id = user['id']
	profile_id = request.forms.get('profile_id')
	try:
			my_profile =  model.Profiles.update(firstname, surname, image, user_id)
			if my_profile:
				return template("profile", my_profile=my_profile)
	except MySQLdb.OperationalError, e:
			return  template("profile", profile_failed = "Something just went wrong")

@get('/profile/view/:id#[1-9]+#')
@authenticate
def view_profile(user, *args, **Kwargs):
	(user, id) = args
		 
	try:
			my_profile =  model.Profiles.view(id)
			if my_profile:
				template("profile", my_profile=my_profile)
			else:
				return template("profile")
	except MySQLdb.OperationalError, e:
			return  template("profile", profile_failed = "Something just went wrong")

	
@post('/login')
def login_submit():
		 email = request.forms.get('email')
		 password = request.forms.get('password')
		 try:
			user =  model.Users.find_user_by_password_and_email(password, email)
			if user:
				  user_session(user['id'])
				  return template("layout", title="Maamariga",  my_test=user["username"])

			else:
                                 return  redirect('/alogin') # template("failedlogin")
		 except MySQLdb.OperationalError ,e:
			return  redirect('a/login') # template("failedlogin")

	
#debug(True)
#run(reloader=True)	
run(app=my_app)