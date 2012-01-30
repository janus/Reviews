from bottle import Bottle, request,  redirect, run
from beaker.middleware import SessionMiddleware
from model.model import  Users
import MySQLdb

app_others = Bottle()
session_opts = {'session.type': 'file','session.cookie_expires': 300, 'session.data_dir': './data','session.auto': True }
new_app = SessionMiddleware(app_others, session_opts)
success_message = "Your account was successfully created. Please activate your account from a mail sent to your email box"
error_message = "Something is wrong with your data, please go through them and edit"

def logged_in_user():
    s = request.environ.get('beaker.session')
    try:
	if s["user_id"]:
	    try:
		return Users.find_by_id(s['user_id']) 
	    except MySQLdb.OperationalError, e:
		raise
    except KeyError, e:
	return  None


def add_url(url):
    s = request.environ.get('beaker.session')
    s['url'] = url
    s.save()

def add_token(token):
    s = request.environ.get('beaker.session')
    s['token'] = token
    s.save()
    return token

def has_user_logged_in():
  s = request.environ.get('beaker.session')
  return True if s.has_key("user_id") else False

def user_session(user_id):
    s = request.environ.get('beaker.session')
    s['user_id'] = user_id
    s.save()
    
def authenticate(url):
    def decorate(handler):
        def _check_auth(*args,**kwargs):
            s = request.environ.get('beaker.session')
            if s['user_id']:
                return handler( *args, **Kwargs)
	    else:
		add_url(url)
                redirect('/login')
        return _check_auth
    return decorate
    
#run(app = new_app)
