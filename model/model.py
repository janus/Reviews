import sys
import MySQLdb
import MySQLdb.cursors
import prevalidate 
import passtest
import helper
import datetime

conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "janus05", db = "myseun",cursorclass=MySQLdb.cursors.DictCursor)
                                                  

class mySQL:
    def __init__(self ):
		pass
		
		
    @classmethod
    def myfetch_once(self, myQuery):
	try:
	    cursor = conn.cursor( )
	    cursor.execute(myQuery)
	    orders = cursor.fetchone( )
	    cursor.close( )
	    return orders
	except MySQLdb.OperationalError, e:
	    raise 
			
    @classmethod
    def fetchall(self, myQuery):
        try:
	    cursor = conn.cursor( )
	    cursor.execute(myQuery)
	    orders = cursor.fetchall( )
	    cursor.close( )
	    return orders
	except MySQLdb.OperationalError, e:
	    raise
			
    @classmethod
    def executeBatch(self, myQuery):
	try:
	    cursor = conn.cursor( );
	    cursor.execute(myQuery);
	    orders = cursor.fetchall( );
	    cursor.close( );
	    return orders
	except MySQLdb.OperationalError, e:
	    raise 
		
    @classmethod		
    def  insert(self, myQuery):
	try:
	    cursor = conn.cursor( )
	    cursor.execute(myQuery)
	    cursor.close( )
	    return True
	except  MySQLdb.OperationalError ,e :
	    raise 


class Comments(mySQL):
    @classmethod
    def create(cls, user_id=None, review_id=None, entry=None):
	return cls(user_id, review_id, entry)
	
    def __init__(self, user_id=None, review_id=None, entry=None):
	self.user_id = user_id
	self.review_id = review_id
	self.entry = entry
	self.user = None
	self.review = None


    def   save(self ):

	if prevalidate.validate_entry(entry):
	    query = """insert into comments 
			(user_id, review_id, entry)
			values(%d, %d,  '%s') """ % (self.user_id, self.review_id,  self.entry) 
	else:
	    return self
	try:
	    mySQL.insert(query)
	    self.review = Review.get_by_id(review_id)
	    self.comments = self.get_by_review_id()
	    return  self
	except MySQLdb.OperationalError ,e :
		raise 
		#return something 
    @classmethod
    def get_by_review_id(self, review_id):
	query = """select users.username, comments.message, comments.created_time from comments , users
			      where  comments.user_id = users.id and comments.review_id = %d 
			      """ %(review_id , )
	return mySQL.fetchall(query)


		 
    @classmethod
    def update(self, user_id, comment_id, message, review_id):
	updated_time = helper.get_current_date_time()
	if prevalidate.validate_entry(entry):
	    query = """update reviews
			set message = '%s', updated_time = '%s' 
			where id = %d and user_id = %d""" % (message, updated_time, comment_id, user_id)
	try:
	    return Review.get_by_id(review_id) if mySQL.insert(query) else False 
	except MySQLdb.OperationalError ,e :
	    raise 
			     
class Reviews(mySQL):
    @classmethod
    def create(cls, user_id, sector_id, title, entry,  url):
	return cls(user_id, sector_id, title, entry,  url)
	
    def __init__(self, user_id, sector_id, title, entry,  url):
	self.user_id = user_id
	self.sector_id = sector_id
	self.title = title
	self.entry = entry
	self.url = url
	

    def   save(self):
        #target_time = helper.get_current_date_time() # modifiy such that you can get time 24 hours less
	hold_valid = [prevalidate.validate_entry(self.entry),  prevalidate.validate_title(self.title)]
	if passtest.mypass(hold_valid):
	    query = """ insert into reviews (entry ,user_id, sector_id, title, url) 
		             values ('%s',  %d, %d, '%s', '%s') """ % (self.entry, self.user_id, self.sector_id, self.title, self.url)
	    myquery = """select user_id, count(*) as mycount from reviews
                         		where user_id = %d 
                                        group by user_id """ %(self.user_id)
	    reviewquery = '''select id from reviews where user_id = %d and  entry = '%s' ''' %(self.user_id, self.entry)
	try:
	    mySQL.insert(query)
	    review_result =  mySQL.myfetchall(reviewquery) 
	    your_data  = mySQL.myfetch_once(myquery)
	    if your_data['mycount'] == 1:
		yourquery = "insert into votes (ID1, ID2, review_id) values (%d, %d, %d)" % (user_id, user_id,  review_result['id'])
		mySQL.insert(yourquery)
		anotherquery = '''select reviews.entry, reviews.title, reviews.url, reviews.created_time,users.username,
								  (select counted_votes from votes where votes.ID2 = %d) as yourvote
					                          from reviews, users  where reviews.user_id = users.id and users.id = %d and reviews.id = %d''' %(user_id, user_id, review_result['id'])
		return  mySQL.myfetch_once(anotherquery)    #"/".join(created_time().split(" ")[0].split("-"))
	except MySQLdb.OperationalError ,e :
	    raise
		 
    @classmethod	 
    def   get(cls, review_id, created_time):
	query = """select * from reviews
			      where reviews.id = %d and reviews.created_time = '%s'
			      """ %(review_id, created_time)
	try:
	    result = mySQL.myfetch_once(query)
	    return [ result,  Comments().listall(review_id)]
	except MySQLdb.OperationalError ,e :
	    raise
		
    @classmethod	 
    def   get_by_url(self, url, created_time):
	query = """select * from reviews
			      where reviews.url = '%s' and reviews.created_time  like  '%s'
			      """ %(review_id, created_time)
	try:
	    result = mySQL.myfetch_once(query)
	    return [ result,  Comments().listall(review_id)]	
	except MySQLdb.OperationalError ,e :
	    raise
		
		
    @classmethod
    def get_by_id(self,  review_id):
	query = """select reviews.branch_id, reviews.user_id, reviews.updated_time, reviews.entry,
	               reviews.title, users.username 
                 	from reviews , users where users.id = reviews.user_id  and  reviews.id =  %d """%(review_id, ) 
	try:
	    result = mySQL.myfetch_once(query)
	    return [ result,  Comments.get_by_review_id(review_id)]
	except MySQLdb.OperationalError ,e :
	    raise
		 
		 
    @classmethod
    def  list_all_reviews_by_user_id(self, user_id, start_point):
	print user_id, start_point
	query = """select reviews.title,reviews.updated_time, reviews.id, reviews.user_id, reviews.entry, reviews.branch_id, users.username from reviews, users 
		              where reviews.user_id = users.id and users.id = %d  limit %d , %d""" %(user_id , start_point, 6)
	try:
	    return mySQL.fetchall(query)
	except MySQLdb.OperationalError ,e :
	    raise 
			
    @classmethod
    def  list_all_reviews(self , start_point=None):
	if start_point is None:
	    query = """select reviews.branch_id, reviews.user_id, reviews.updated_time, reviews.entry,
	              reviews.id, reviews.title, users.username 
                 	from reviews , users where users.id = reviews.user_id """
	else:
	    query = """select reviews.branch_id, reviews.user_id, reviews.updated_time, reviews.entry,
	              reviews.id, reviews.title, users.username 
                 	from reviews , users where users.id = reviews.user_id  """
	try:
	    review =  mySQL.fetchall(query)
	    return review
	except MySQLdb.OperationalError ,e :
	    raise 
		
		 
    @classmethod
    def update(self, user_id,  review_id, entry, title):
	updated_time = helper.get_current_date_time()
	if prevalidate.validate_entry(entry):
	    query = """update reviews
			              set entry = '%s', created_time = '%s' , title = '%s',
                                      where id = %d and user_id = %d""" % (entry, updated_time, title, review_id, user_id)
	    try:
		return True if mySQL.insert(query) else False
	    except MySQLdb.OperationalError, e :
		raise
			             
		 
    @classmethod
    def search(self, search_text, start_point):
	query = """SELECT  reviews.branch_id, reviews.user_id, reviews.updated_time, reviews.entry,
	reviews.id, reviews.title, users.username 
	from reviews , users 
	WHERE  users.id = reviews.user_id and 
	MATCH(reviews.title, reviews.entry) AGAINST('%s' IN BOOLEAN MODE)  limit %d , %d""" % (search_text, start_point, 6)
	try:
	    return mySQL.fetchall(query)
	except MySQLdb.OperationalError , e:
	    raise


print  Reviews.get_by_id(1)
print  Reviews.list_all_reviews(4)[::-1][0]["updated_time"].strftime("%B %d '%y at %H:%M")
class Votes(mySQL):
    def __init__(self):
	mySQL.__init__(self)
	pass
	
    @classmethod		
    def update(self, user_id, review_user_id, review_id, value):
	qresult = mySQL.myfetch_once("select counted_votes from votes where ID2 = %d and review_id = %d" % (review_user_id, review_id))
	query = """insert into votes (insert into votes (ID1, ID2, review_id, counted_votes)
                 		values (%d, %d, %d, %d) """ % (user_id, review_user_id, review_id, ( qresult['counted_votes'] + value))
	try:
	    return True if mySQL.insert(query) else False
	except MySQLdb.OperationalError, e :
	    raise
			
           		
 
		 
class Users(mySQL):
    def __init__(self):
	mySQL.__init__(self)
	pass
		
	
    @classmethod
    def   create(self, username, email, activation_code, password):
	created_time  =  helper.get_current_date_time()
	flag = 0
	hold_valid = [prevalidate.validate_username(username), prevalidate.validate_email(email), prevalidate.validate_password(password),prevalidate.validate_time(created_time)]
	if passtest.mypass(hold_valid) is True:
	    (salt, password) =  helper.password_salt(password)
	    myquery = "INSERT INTO users (username ,created_time,updated_time,email ,salt,activation_code,password )VALUES('%s', '%s', '%s',  '%s', '%s', '%s', '%s')" %(username ,created_time,created_time,email ,salt,activation_code,password )
	    try:
		 return True if mySQL.insert(myquery) else False 
	    except MySQLdb.OperationalError, e :
		raise
                     			 
		 
    @classmethod	 
    def   update_password(self, user_id, password):
	hold_valid = [prevalidate.validate_password(password)]
	if passtest.mypass(hold_valid) is True:
	    (salt, password) =  helper.password_salt(password)
	#updated_time  =  helper.get_current_date_time()
	myquery = "update users set password = '%s', salt = '%s' " % (password, salt)
	myquery = myquery + "  where id = %d" % (user_id, )
	try:
	    return True if mySQL.insert(myquery) else False 
	except MySQLdb.OperationalError, e :
	    raise
			 
			 

    @classmethod
    def find_user_by_password_and_email(self, password, email):
	hold_valid = [prevalidate.validate_password(password), prevalidate.validate_email(email)]
	if passtest.mypass(hold_valid) is True:
	    myquery = """select * from users  where email = '%s'  and flag = 1""" % (email, )
	    try:
		myresult =  mySQL.myfetch_once(myquery)
		if myresult is None:
		    return False
		(salt, password) = helper.password_salt(password, myresult['salt'])
		return myresult if  password  == myresult['password'] else False 
	    except MySQLdb.OperationalError , e:
		raise
		
    @classmethod
    def find_by_id(self, user_id):
	myquery = """select * from users  where id = %d """ % (user_id,)
	try:
	    
	    result = mySQL.myfetch_once(myquery)
	    print result 
	    return result if result  else None 
	except MySQLdb.OperationalError , e:
	    raise
	    
    @classmethod
    def activate(self, activation_number):
	myquery = """update users set flag = %d 
		                   where activation_code = '%s'""" %(1, activation_number)
	try:
	    return mySQL.insert(myquery)
	except MySQLdb.OperationalError , e:
	    raise
    @classmethod
    def reset_password(self, email):
	if prevalidate.validate_email(email):
	    myquery = """select * from users  where  email = '%s'""" %(email)
	    try:
	        if mySQL.myfetch_once(myquery):
		    password, salt, hashed_password = helper.generate_password_and_salt()
		    query = """update users set password = '%s', salt = '%s' """ % (hashed_password, salt)
		    mySQL.insert(query)
		    return password
	    except MySQLdb.OperationalError , e:
	        raise
#print Users.reset_password("satajanus@gmail.com")

	
class Profiles(mySQL):
    def __init__(self):
	mySQL.__init__(self)
	pass
		
	
    @classmethod
    def   create(self, firstname, surname, image, user_id):
	flag = 0
	hold_valid = [prevalidate.validate_username(username), prevalidate.validate_email(email), prevalidate.validate_password(password)]
	if passtest.mypass(hold_valid) is True:
	    (salt, password) =  helper.password_before_save(password)
	    myquery = "INSERT INTO users (firstname, surname,location, job_title, user_id ) VALUES ('%s', '%s', '%s', %d, '%s', '%s', %d)" %(firstname, surname,location, job_title, user_id )
	    try:
		return mySQL.insert(myquery)
	    except MySQLdb.OperationalError, e :
		raise

		 
    @classmethod	 
    def   update(self, user_id, password):
	pass 
		 
    @classmethod	 
    def get(self, user_id):
	query = "select * from profiles where user_id = %d" % user_id
	try:
	    return mySQL.myfetch_once(query)
	except MySQLdb.OperationalError ,e:
	    raise 

		 
