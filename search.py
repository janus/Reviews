from bottle import  request,  template, run, debug
import MySQLdb
from model.model import  Reviews
import reviews
import user_helper
import main
from session import app_others,new_app

@app_others.route('/search')
def search():
    search  = request.GET.get('asearch').strip()
    try:
	start_point = 1
	reviews = Reviews.search(search, start_point)
	return template("list_reviews", reviews = reviews ,   start_point = start_point) 
    except MySQLdb.OperationalError, e:
	redirect("/index")
	
debug(True)
run(app = new_app)
