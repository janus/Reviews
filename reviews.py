from bottle import  request, template, redirect,debug,validate, run
from model import helper
import mail
import MySQLdb
from model.model import  Reviews, Comments
from session import app_others, logged_in_user, add_url, new_app



@app_others.get('/review/:a/:b/:c/:name')
@validate(a=int, b=int, c=int)
#get out validated
def get_review(a, b , c, name):
    created_time =  "{}-{}-{}".format(a ,b , c)
    try:
        review, comments = Reviews.get_by_url(created_time, name.strip())
	if review:
	    return template("review", review = review, comments=comments)
	else:
	    redirect('/index')
    except MySQLdb.OperationalError, e:
	redirect('/index')

@app_others.get('/reviews/:id')
def get_review_id(id):
    id = int(id)
    try:
	review, comments = Reviews.get_by_id( id)
	if review:
	    return template("review",  review = review, comments=comments)
	else:
	    redirect('/index')
    except MySQLdb.OperationalError, e:
	redirect('/index')
		
@app_others.route('/reviews')
def get_all_Reviews():
    try:
        start_point = 1
	reviews =  Reviews.list_all_reviews()
	reviews = reviews[::-1]
	reviews = reviews[:6]
	if reviews :
	    #start_point = str(start_point)
	    return template("list_reviews", reviews = reviews , start_point=start_point) #I need to add pagination somewhere, and 
	else:
	    return template("list_reviews", reviews=reviews, start_point=start_point)
    except MySQLdb.OperationalError, e:
	redirect('/index')

@app_others.route('/reviews/pages')
def get_page():
    start_point = request.GET.get("start")
    try:
        start_point = int(start_point)
    except ValueError, e:
	redirect("/index")
    try:
        reviews = Reviews.list_all_reviews()
	reviews = reviews[::-1]
	reviews = reviews[start_point:6+start_point]
	return template("list_reviews" , reviews = reviews, start_point=start_point)
    except MySQLdb.OperationalError, e:
	redirect('/index')
    
@app_others.get('/review/edit/:id')
def review_edit_page(id):
    user = logged_in_user()
    if not user:
	add_url( "/reviews/edit/{}".format(id))
	redirect("/login")
    else:
	review = Reviews.get_by_id(id)
        return template("review", review = review)

#Work from here down ... a lot needs to be changed

@app_others.get('/reviews/user')
def reviews_user():
    user_id = request.GET.get("id")
    start_point = 1
    try:
	user_id = int(user_id)
    except ValueError, e:
	redirect("/index")
    try:
	reviews = Reviews.list_all_reviews_by_user_id(user_id, start_point)
	return template("search_reviews" , reviews = reviews, start_point = start_point)
    except MySQLdb.OperationalError, e:
	redirect("/index")

@app_others.get('/reviews/users')
def reviews_users():
    start_point = request.GET.get("start")
    user_id = request.GET.get("id")
    try:
	start_point = int(start_point)
	user_id = int(user_id)
    except ValueError, e:
	redirect("/index")
    try:
	reviews = Reviews.list_all_reviews_by_user_id(user_id, start_point)
	return template("search_reviews" , reviews = reviews, start_point = start_point)
    except MySQLdb.OperationalError, e:
	redirect("/index")

@app_others.post('/review/edit')
def edit_review():
    title =  request.forms.get('title').strip()
    entry =  request.forms.get('entry').strip()
    review_id =  request.forms.get('review_id').strip()
    try:
	logged_id = logged_in_user()["id"]
    except KeyError, e:
	redirect("/index")
    try:
	if logged_id:
	    status = Reviews.update(logged_id,  review_id, entry, title)
	    if status:
		link = "/review/%d/%s" %(review_id, "You just updated your review") # This is wrong ...
		redirect(link)
	    else:
		redirect('/index')
	else:
	    redirect('/index')
    except MySQLdb.OperationalError ,e:
	redirect('/index')
	
@app_others.get('/review/create')
def create_review():
    try:
        user = logged_in_user()
        if not user:
	    add_url('/review/create')
            redirect('/login')
        else:
	    reviews = Reviews.list_all_reviews()
	    return template("create_review", user_id=user["id"], my_top = user["username"], reviews = reviews)
    except MySQLdb.OperationalError , e:
	redirect('/index')

#Todo be filtered morrow
@app_others.post('/review/create')
def create_review():
    title =  request.forms.get('title').strip()
    branch_id =  request.forms.get('sector_id').strip()
    id =  request.forms.get('id').strip()
    message =  request.forms.get('message').strip()
    user_details  = logged_in_user()
    url = generate_url(user_details["surname"], title)
    try:
	review =  Reviews.create(id, branch_id, title, message,  url).save()
	if review:
	    return  template("review",  review = review)
	else:
	    redirect('/index')
    except MySQLdb.OperationalError , e:
	redirect('/index')

#Todo be filtered morrow
@app_others.post('/comment/create')
def create_comment():
    message =  request.forms.get('message').strip()
    review_id =  request.forms.get('review_id')
    s = request.environ.get('beaker.session')
    user_id = logged_in_user()['id']
    try:
	status =  Comments.create(user_id, review_id, message)
	review, comments = Reviews.get_by_id( review_id)
	if status:
	    return template("review" , review = review, comments= comments)
	else:
	    return template("review_error", message = "Failed to create your model.Comments", review = review, comments=comments)
    except MySQLdb.OperationalError , e:
	return template("review_error", message = "Failed to create your model.Comments", review = review, comments=comments)

@app_others.get('/review/edit/:id')
def edit_comment_page(id):
    if not  logged_in_user():
	url = "review/edit/%s" % id
	add_url(url)
	redirect('/alogin')
	
@app_others.post('/review/edit')
def edit_comment():
    message =  request.forms.get('message').strip()
    comment_id =  request.forms.get('comment_id').strip()
    s = request.environ.get('beaker.session')
    logged_id = logged_in_user()['id']
    if user_id == logged_id:
	try:
	    status = Comments.update(logged_id,  comment_id, message)
	    if status:
		link = "/review/%d/%s" %(review_id, "You just updated your comment") 
		redirect(link)
	    else:
		redirect('/index')
	except MySQLdb.OperationalError ,e:
	    redirect('/index')
	else:
	    redirect('/index')
			

#debug(True)
#run(app = new_app)
