import sys
import MySQLdb
import MySQLdb.cursors
import prevalidate 
import passtest
import helper



conn = MySQLdb.connect (host = "localhost",
                           user = "root",
                           passwd = "janus05",
                           db = "myseun",cursorclass=MySQLdb.cursors.DictCursor)

   
#cursor = conn.cursor ()


class mySQL:
    
	def __init__(self ):
		pass
		
	@classmethod
	def myfetchOnce(self, myQuery):

			cursor = conn.cursor( )
			cursor.execute(myQuery)
			orders = cursor.fetchone( )
			cursor.close( )
			return orders

        @classmethod
	def iexecuteBatch(self, myQuery):
		try:
			cursor = conn.cursor( )
			cursor.execute(myQuery)
			orders = cursor.fetchall( )
			cursor.close( )
		except:
			print "Error retrieving orders."
			conn.close( )
			exit(0)
			
		return orders
		
	@classmethod
	def insert(self, myquery):

			cursor = conn.cursor()
			cursor.execute(myquery)

		
	@classmethod		
	def  myWay(self, kool):
	        mySQL.myprint(kool)
		
	@classmethod
	def myprint(self, kool):
		mytep = kool + " loop"
		print(mytep)




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
			 myquery = "INSERT INTO users (username ,created_time,updated_time,flag,email ,salt,activation_code,password ) VALUES ('%s', '%s', '%s', %d, '%s', '%s', '%s', '%s')" %(username ,created_time,created_time,flag,email ,salt,activation_code,password )
		 mySQL.insert(myquery) 

 
		 
	@classmethod	 
	def   update(self, user_id, password):
		 return [review, comments]	

	def find_password_and_email(password, email):
		return 
		
	@classmethod	 
	def   update_password(self, user_id, password):
		 (salt, password) =  helper.password_salt(password)
		 updated_time  =  helper.get_current_date_time()
		 myquery = "update users set password = '%s', salt = '%s' , updated_time = '%s'" % (password, salt, updated_time)
		 myquery = myquery + "  where id = %d" % user_id
		 mySQL.insert(myquery) 
		 
	@classmethod
	def find_password_and_email(self, password, email):
		myquery = """select * from users  where email = '%s' """ % email
		myresult =  mySQL.myfetchOnce(myquery)
		(salt, password) = helper.password_salt(password, myresult['salt'])
		if password  == myresult['password']:
			print myresult
		else:
		       return False 
			 
Users.find_password_and_email( 'kobdadddbbxygssgs','haacvvccop@cmail.com' )	