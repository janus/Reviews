from bottle import route, run, template, static_file

#print template('block_content', title='Hello World!')
#TEMPLATE_PATH.insert(0,'/home/rmicro/myPython/myseunPython/myscript/views')



@route('/hello/:name')
def index(name='World'):
     return  template('block_content', title='Hello World!')
      

#print template('block_content', title='Hello World!')

#from bottle import static_file
@route('/static/:filename')
def server_static(filename):
    return static_file(filename, root='/home/rmicro/myPython/myseunPython/myscript/views')
    
    
run(host='localhost', port=8080)