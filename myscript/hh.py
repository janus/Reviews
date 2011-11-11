from bottle import get, post, request, run, route, TEMPLATE_PATH, template

print TEMPLATE_PATH

print template('content', content='Hello World!')


@route('/hello/:name')
def index(name='World'):
     return  template('block_content', title=name)


     
     
#@route('/login')
@get('/login')
def login_form():
    return '''<form method="POST">
<input name="name"
type="text" />
<input name="password" type="password" />
<type = "submit" value="Me" />
</from>'''
#@route('/login', method='POST')
@post('/login')
def login_submit():
         name = request.forms.get('name')
         password = request.forms.get('password')
         if check_login(name, password):
               return "<p>Your login was correct</p>"
         else:
	       return "<p>Login failed</p>"

     
run(reloader = True ,host='localhost', port=8080)


#07029993654

