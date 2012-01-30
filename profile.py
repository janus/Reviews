from bottle import run, app, route, request, get, post, static_file, template, redirect,debug,validate
from beaker.middleware import SessionMiddleware
import mail
import MySQLdb
from model.model import  model , helper
from search import user_app



@post('/profile/create')
@authenticate
def create_profile():
    firstname = form_get('firstname').strip()
    surname = form_get('surname').strip()
    image = request.file.get('image')
    user_id = logged_in_user()['id']
	try:
	    my_profile =  model.Profiles.create(firstname, surname, image, user_id)
	    if my_profile:
		return template("profile", my_profile=my_profile)
	except MySQLdb.OperationalError , e:
		return  template("profile", profile_failed = "Something just went wrong")
	
@post('/profile/edit')
@authenticate
def edit_profile():
    firstname = form_get('firstname').strip()
    surname = form_get('surname').strip()
    image = request.file.get('image')  #To do
    user_id = user['id']
    profile_id =form_get('profile_id')
	try:
	    my_profile =  model.Profiles.update(firstname, surname, image, user_id)
	    if my_profile:
		return template("profile", my_profile=my_profile)
	except MySQLdb.OperationalError, e:
	    return  template("profile", profile_failed = "Something just went wrong")

@get('/profile/view/:id#[1-9]+#')
def view_profile():
    try:
	my_profile =  model.Profiles.view(id)
	if my_profile:
	    template("profile", my_profile=my_profile)
	else:
	    return template("profile")
	except MySQLdb.OperationalError, e:
	    return  template("profile", profile_failed = "Something just went wrong")
