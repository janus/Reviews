import sys
import MySQLdb
import MySQLdb.cursors
import prevalidate 
import passtest
import helper



try:
                   conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "janus05", db = "myseun",cursorclass=MySQLdb.cursors.DictCursor)
except MySQLdb.OperationalError, e:
		raise

                                                    

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

	def __init__(self):
		mySQL.__init__(self)
		pass
		
	
	@classmethod
	def   create(self, *message):
		created_time = helper.get_current_date_time()
		(user_id, review_id,  entry) = 	message
		hold_valid = [prevalidate.validate_entry(entry), prevalidate.validate_time(created_time)]
		if passtest.mypass(hold_valid) is True:
	             query = """insert into comments 
		                  (user_id, review_id, updated_time, created_time, message)
				  values(%d, %d, '%s','%s', '%s') """ % (user_id, review_id, updated_time, created_time, entry) 
		     try:
		           if mySQL.insert(query):
			      return True
		     except MySQLdb.OperationalError ,e :
			     raise 
		#return something 

        @classmethod
	def  listall(self, review_id):
		query = "select * from comments where review_id = %d" % review_id
		try:
			result_set = mySQL.fetchall(query)
			return result_set
		except MySQLdb.OperationalError ,e :
			raise
		
	@classmethod	 
	def   get(self, created_time, name):
		 return [review, comments]	
		 
	@classmethod
	def update(self, user_id, comment_id, message):
		updated_time = helper.get_current_date_time()
		if prevalidate.validate_entry(entry):
			query = """update reviews
			              set message = '%s', updated_time = '%s' 
                                      where id = %d and user_id = %d""" % (message, updated_time, comment_id, user_id)
		        try:
		           if mySQL.insert(query):
			      return True
		        except MySQLdb.OperationalError ,e :
			     raise 
			     
class Reviews(mySQL):

	def __init__(self):
		mySQL.__init__(self)
		pass
		
	
	@classmethod
	def   create(self, *message):
		(user_id, sector_id, company_id, branch_id, title, entry,  url)  = message
		created_time  =  helper.get_current_date_time()
		hold_valid = [prevalidate.validate_entry(entry), prevalidate.validate_time(created_time), prevalidate.validate_title(title)]
		if passtest.mypass(hold_valid) is True:
			query = """ insert into reviews (entry , created_time, user_id, branch_id, title, url) 
		             values ('%s', '%s', %d, %d, '%s', '%s') """ % (entry, created_time, user_id, branch_id, title, url)
			myquery = """select user_id, count(*) as mycount from reviews
                         		where entry = '%s' and user_id = %d and created_time = '%s'
                                        group by user_id """ %(entry, user_id, created_time)
			reviewquery = '''select id from reviews where user_id = %d and created_time = '%s' and entry = '%s' ''' %(user_id, created_time, entry)
			try:
				mySQL.insert(query)
				review_result =  mySQL.myfetch_once(reviewquery) 
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
	def   get(self, review_id, created_time):
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
		query = """select * from reviews
			      where reviews.id = %d 
			      """ %(review_id)
		try:
			result = mySQL.myfetch_once(query)
			return [ result,  Comments().listall(review_id)]
		except MySQLdb.OperationalError ,e :
			raise
		 
		 
	@classmethod
	def  list_all_review_by_user_id(self, user_id):
		query = """select reviews.title,reviews.created_time, reviews.id, users.username from reviews, users 
		              where reviews.user_id = users.id and users.id = %d""" %(user_id)
		try:
			result = mySQL.fetchall(query)
			return result
		except MySQLdb.OperationalError ,e :
			raise 
			
	@classmethod
	def  list_all_reviews(self):
		query = """select * from reviews"""
          	result = mySQL.fetchall(query)
		try:
			result = mySQL.fetchall(query)
			return result
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
				mySQL.insert(query)
				return True
			except MySQLdb.OperationalError, e :
				raise
			             
		 
	@classmethod
	def search(self, search_text):
		query = "SELECT  * from reviews WHERE  MATCH(title, entry) AGAINST('%s' IN BOOLEAN MODE)" % search_text
	        try:
			result_set = mySQL.fetchall(query)
			return result_set
		except MySQLdb.OperationalError , e:
			raise
print Reviews.search("branches")



class Votes(mySQL):
	def __init__(self):
		mySQL.__init__(self)
		pass
		
	def update(self, user_id, review_user_id, review_id, value):
		qresult = mySQL.myfetch_once("select counted_votes from votes where ID2 = %d and review_id = %d" % (review_user_id, review_id))
		query = """insert into votes (insert into votes (ID1, ID2, review_id, counted_votes)
                 		values (%d, %d, %d, %d) """ % (user_id, review_user_id, review_id, ( qresult['counted_votes'] + value))
		try:
			mySQL.insert(query)
			return True
		except MySQLdb.OperationalError, e :
			raise
			
           		
	 
		 
class Users(mySQL):

	def __init__(self):
		mySQL.__init__(self)
		pass
		
	
	@classmethod
	def   create(self, username, email, activation_code, password):
		 print email
		 created_time  =  helper.get_current_date_time()
		 flag = 0
		 hold_valid = [prevalidate.validate_username(username), prevalidate.validate_email(email), prevalidate.validate_password(password),prevalidate.validate_time(created_time)]
	         if passtest.mypass(hold_valid) is True:
			(salt, password) =  helper.password_salt(password)
			myquery = "INSERT INTO users (username ,created_time,updated_time,email ,salt,activation_code,password )VALUES('%s', '%s', '%s',  '%s', '%s', '%s', '%s')" %(username ,created_time,created_time,email ,salt,activation_code,password )
			try:
				foo = mySQL.insert(myquery)
				print foo
				return True
				
			except MySQLdb.OperationalError, e :
				raise
                     			 
		 
	@classmethod	 
	def   update_password(self, user_id, password):
		 hold_valid = [prevalidate.validate_password(password)]
		 if passtest.mypass(hold_valid) is True:
			(salt, password) =  helper.password_salt(password)
			updated_time  =  helper.get_current_date_time()
			myquery = "update users set password = '%s', salt = '%s' , updated_time = '%s'" % (password, salt, updated_time)
			myquery = myquery + "  where id = %d" % user_id
			try:
				mySQL.insert(myquery)
				return True
			except MySQLdb.OperationalError, e :
				raise
			 
			 

	@classmethod
	def find_user_by_password_and_email(self, password, email):
		hold_valid = [prevalidate.validate_password(password), prevalidate.validate_email(email)]
		if passtest.mypass(hold_valid) is True:
			
			myquery = """select * from users  where email = '%s' """ % email
		
		#print "I am here"
			try:
				myresult =  mySQL.myfetch_once(myquery)
				if myresult is None:
					return False
				(salt, password) = helper.password_salt(password, myresult['salt'])
				if password  == myresult['password']:
					return myresult
				else:
					return False 
			except MySQLdb.OperationalError , e:
				raise
				
	@classmethod
	def activate(self, activation_number):
		print "LOOP"
		myquery = """update users set flag = %d 
		                   where activation_code = '%s'""" %(1, activation_number)
		try:
		      return mySQL.myfetch_once(myquery)
		except MySQLdb.OperationalError , e:
				raise
#print Users.update_password(1, "emeka78dhjdlk")

	
class Profiles(mySQL):

	def __init__(self):
		mySQL.__init__(self)
		pass
		
	
	@classmethod
	def   create(self, firstname, surname, image, user_id):
		 created_time  =  helper.get_current_date_time()
		 flag = 0
		 hold_valid = [prevalidate.validate_username(username), prevalidate.validate_email(email), prevalidate.validate_password(password),prevalidate.validate_time(created_time)]
	         if passtest.mypass(hold_valid) is True:
			 (salt, password) =  helper.password_before_save(password)
			 myquery = "INSERT INTO users (firstname, surname,created_time,updated_time,location, job_title, user_id ) VALUES ('%s', '%s', '%s', %d, '%s', '%s', %d)" %(firstname, surname,created_time,updated_time,location, job_title, user_id )
			 try:
				return mySQL.insert(myquery)
			 except MySQLdb.OperationalError, e :
				raise
		 return False
                     			 
		 
	@classmethod	 
	def   update(self, user_id, password):
		pass 
		 
	@classmethod	 
	def get(self, user_id):
		 query = "select * from profiles where user_id = %d" % user_id
		 try:
			 result = mySQL.myfetch_once(query)
			 return result
		 except MySQLdb.OperationalError ,e:
			    raise 

		 
