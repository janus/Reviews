from bottle import  request, template, redirect,debug,validate, run
from model import helper
import mail
import MySQLdb
from model.model import  Reviews, Comments, Votes
from session import app_others, logged_in_user, add_url, new_app


def return_reviews():
    return Reviews.list_all_reviews()[::-1][:6]

@app_others.get('/review/:a/:b/:c/:name')
@validate(a=int, b=int, c=int)
#get out validated
def get_review(a, b , c, name):
    created_time =  "{a}-{b}-{c}".format(a ,b , c)
    try:
        review, comments = Reviews.get_by_url(created_time, name.strip())
	if review:
	    return template("review", review = review, comments=comments)
	else:
	    redirect('/index')
    except MySQLdb.OperationalError, e:
	redirect('/index')

@app_others.get('/reviews/sector')
def get_sector_review():
    try:
	    
        sector_id =  request.GET.get("sector_id")
        start_point = int(request.GET.get("start"))
	print sector_id, start_point
	sector_reviews = Reviews.get_sector_by_id(int(sector_id))[::-1][start_point:6+start_point]
	print sector_reviews
        user_details = logged_in_user()
        my_top = user_details ["username"] if user_details  else 0	
        reviews = return_reviews()
        return  template("sector_activity", sector_reviews=sector_reviews, reviews=reviews, my_top = my_top, start_point = start_point )		
    except (MySQLdb.OperationalError, ValueError):
	redirect('/index')

@app_others.get('/sector/:id')
def get_sector(id):
    sector_reviews = Reviews.get_sector_by_id(int(id))[::-1][:6]
    try:
	start_point = 1
	user_details = logged_in_user()
	my_top = user_details ["username"] if user_details  else 0	
	reviews = return_reviews()
	return  template("sector_activity", sector_reviews=sector_reviews, reviews=reviews, my_top = my_top, start_point = start_point)		
    except MySQLdb.OperationalError, e:
	redirect('/index')
	
	
@app_others.get('/reviews/:id')
def get_review_id(id):
    id = int(id)
    try:
	review, comments = Reviews.get_by_id( id)
	if review:
	    user = logged_in_user()
	    my_top = user["username"] if user is not None else 0
	    reviews =  Reviews.list_all_reviews()
	    return template("review",  review = review, comments=comments, reviews= reviews, my_top=my_top)
	else:
	    redirect('/index')
    except MySQLdb.OperationalError, e:
	redirect('/index')
		
@app_others.route('/reviews')
def get_all_Reviews():
    try:
        start_point = 1
	reviews =  return_reviews()
	if reviews :
	    user = logged_in_user()
	    my_top = user["username"] if user is not None else 0
	    return template("list_reviews", reviews = reviews , start_point=start_point, my_top=my_top) #I need to add pagination somewhere, and 
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
        reviews = Reviews.list_all_reviews()[::-1][start_point:6+start_point]
	user = logged_in_user()
	my_top = user["username"] if user is not None else 0
	return template("list_reviews" , reviews = reviews, start_point=start_point,my_top=my_top)
    except MySQLdb.OperationalError, e:
	redirect('/index')
    
@app_others.get('/review/edit/:id')
def review_edit_page(id):
    id = int(id)
    try:
        user = logged_in_user()
        if not user:
	    add_url( "/review/edit/{}".format(id))
	    redirect("/login")
        else:
	    reviews =  return_reviews()
	    (review, _) = Reviews.get_by_id( id)
            return template("review_edit", review = review, reviews=reviews, my_top = user["username"])
    except MySQLdb.OperationalError, e:
	redirect("/index")

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
    review_id =  int(request.forms.get('review_id').strip())
    branch_id =  int(request.forms.get('option-value'))
    #id =  request.forms.get('id')
    try:
	user_details  = logged_in_user()
	id = user_details["id"]
	url = helper.generate_url(user_details["username"], title)
    except TypeError, e:
	redirect("/index")
    try:
	if id:
	    status = Reviews.update(id,  review_id, entry, title, url,  branch_id) 
	    if status:
		redirect('/reviews/{}'.format(review_id))
	    else:
		redirect('/index')
	else:
	    redirect('/index')
    except MySQLdb.OperationalError ,e:
	redirect('/index')
	
@app_others.get('/review/create')
def create_review_get():
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

@app_others.post('/review/create')
def create_review_post():
    title =  request.forms.get('title').strip()
    branch_id =  request.forms.get('option-value')
    message =  request.forms.get('entry').strip()
    branch_id = branch_id
    try:
	user_details  = logged_in_user()
	id = user_details["id"]
	url = helper.generate_url(user_details["username"], title)
	review_id =  Reviews(id, branch_id, title, message,  url).save()
	reviews = return_reviews()
	if review_id:
	    review, comments = Reviews.get_by_id(int(review_id))
	    return  template("review",  review = review, reviews =reviews, comments = comments, my_top = user_details["username"])
	else:
	    redirect('/index')
    except MySQLdb.OperationalError , e:
	redirect('/index')

@app_others.post('/comment/create')
def create_comment():
    message = request.forms.get('articleComment').strip()
    review_id =  request.forms.get('review_id')
    s = request.environ.get('beaker.session')
    if logged_in_user() is None:
	redirect('/login')
    else:
	try:
	    user_details = logged_in_user()
	    user_id = user_details['id']
	    reviews =  return_reviews()
	    (review, comments) =  Comments.create(user_id, review_id, message).save()
	    #review, comments = Reviews.get_by_id( review_id)
	    if comments:
	        return template("review" , review = review, comments= comments, my_top = user_details["username"], reviews = reviews)
	    else:
	        return template("review_error", message = "Failed to create your model.Comments", review = review, comments=comments)
        except MySQLdb.OperationalError , e:
	    return template("review_error", message = "Failed to create your model.Comments", review = review, comments=comments)

@app_others.get('/votes/up/:id')
def vote_up(id):
    try:
	logged_id = logged_in_user()['id']
    except TypeError, e:
	redirect('/reviews/{}'.format(id))
    try:
	review, comments = Reviews.get_by_id( id)
	if review['user_id'] == logged_id:
	    redirect('/reviews/{}'.format(id))
	elif Votes.get_by_review_id_and_user_id(logged_id, id):
	    redirect('/reviews/{}'.format(id))
	else:
	   voted = Votes.insert(review['user_id'], logged_id, id, 5)
	   redirect('/reviews/{}'.format(id))
    except MySQLdb.OperationalError , e:
	redirect('/reviews/{}'.format(id))
		
@app_others.get('/votes/down/:id')
def vote_down(id):
    try:
	logged_id = logged_in_user()['id']
    except TypeError, e:
	redirect('/reviews/{}'.format(id))
    try:
	review, comments = Reviews.get_by_id( id)
	if review['user_id'] == logged_id:
	    redirect('/reviews/{}'.format(id))
	elif Votes.get_by_review_id_and_user_id(logged_id, id):
	    redirect('/reviews/{}'.format(id))
	elif review['review_votes'] is None or review['review_votes'] == 1:
	    redirect('/reviews/{}'.format(id))
	else:
	   voted = Votes.insert(review['user_id'], logged_id, id, -2 )
	   redirect('/reviews/{}'.format(id))
    except MySQLdb.OperationalError , e:
	redirect('/reviews/{}'.format(id))
		

#debug(True)
#run(app = new_app)

