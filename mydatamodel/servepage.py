from bottle import get, post, request
#@route('/login')
@get('/login')
def login_form():
return '''<form method="POST">
<input name="name"
type="text" />
<input name="password" type="password" />
</from>'''
#@route('/login', method='POST')
@post('/login')
