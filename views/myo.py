from bottle import route, install, template

print template('block_content', title='Hello World!')