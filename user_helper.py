from bottle import run, app, route, request, get, post, static_file, template, redirect,debug,validate, Bottle
import mail
import MySQLdb
from model.model import  Users , helper
from session import app_others,logged_in_user, success_message, error_message, add_token


@app_others.get('/register')
def get_user_form():
    token = add_token(helper.token)
    my_top, my_bottom = 1 , 1
    return template("user_registration_form", title="Maamariga", my_top = my_top, 
                      cond = 0, my_bottom=my_bottom, token=token )


@app_others.post('/register')
def create_user():
    username = request.forms.get('username').strip()
    email       =  request.forms.get('email').strip()
    password =  request.forms.get('password').strip()
    conpassword = request.forms.get('conpassword').strip()
    token =  request.forms.get('form_token').strip()
    activation_code = helper.activation_hash()
    user_session = request.environ.get('beaker.session')
    if token == user_session["token"]:
	del user_session["token"]
	if password == conpassword:
	    try:
	       if Users.create(username, email, activation_code, password):
		    mymail.send_mail(email=email, name=username, activation_code = activation_code)
		    return template("registration", success_message = success_message,username=username)
	       else:
		    return template("user_registration_form", error_message = error_message, cond=1)
	    except MySQLdb.OperationalError ,e:
	        return template("user_registration_form", error_message = error_message,cond=1)
	else:
	     return  template("user_registration_form",error_message = error_message, cond=1)   


@app_others.get('/user/edit')
def get_edit_user_form():
    try:
	user_details = logged_in_user()
	if user_details:
	    email =  user_details['email']
	    username = user_details['username']
            token = add_token(helper.token)
            return template("edit_user", my_top = 0,  token=token, email=email, username=username)
	else:
	    redirect("/login")
    except MySQLdb.OperationalError ,e:
	redirect("/login")

@app_others.post('/user/edit')
def update_user():
    password =  request.forms.get('password').strip()
    conpassword = request.forms.get('conpassword').strip()
    email = request.forms.get('email').strip()
    user_details = logged_in_user()
    token =  request.forms.get('form_token').strip()
    user_session = request.environ.get('beaker.session')
    if token == user_session["token"]:
	del user_session["token"]
	if user_details["id"]:
	    if password is not '' and conpassword is not '' and password == conpassword:
		try:
		    my_return = Users.update_password(user_details["id"] , password)
		    if my_return:
			mymail.send_mail( email=user_details['email'], name=user_details['username'])
			return template("registration",success_message = success_message,  username=user_details["username"] ) 
		    else:
			 template("edit_user", my_top =0, error_message  = error_message, email = user_details["email"], username=user_details["username"])
			 
		except MySQLdb.OperationalError , e:
		    return  template("edit_user", my_top =0, error_message  = error_message, email = user_details["email"], username=user_details["username"])
	    else:
		redirect("/user/edit")
	else:
	    redirect("/user/edit")
    else:
	 redirect("/user/edit") 

			
@app_others.get('/activation')
def activate_account():
    activation_number = request.GET.get('activate')
    try:
	status = Users.activate(activation_number)
	if status: 
	    return template("activation_message", message ="Your account is now activated" )
	else:
	    return template("activation_message", message = error_message )
    except MySQLdb.OperationalError , e:
	return template("activation_message", message = error_message )
			
@app_others.get('/reset/password')
def reset_password():
    return template("reset_password", message="Please enter your email address")
    
@app_others.post('/reset/password')
def reset_member_password():
    email = request.forms.get('email').strip()
    if email:
	try:
            password = Users.reset_password(email)
	    print password
	    if password:
	        mymail.send_mail( email=email, password=password) 
		return template("registration",success_message = "A new password was sent to your box",  username=email ) 
	    else:
		return template("reset_password", message="Email not in our data store")
	except MySQLdb.OperationalError , e:
	     return template("reset_password", message="Email not in our data store")
    else:
        return template("reset_password", message="Email not in our data store")	    
