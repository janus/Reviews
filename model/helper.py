import hashlib
import random
import datetime
import time

def get_current_date_time():
	now = datetime.datetime.now()
	now = str(now).split(".")
	return now[0]


def random_password():
	my_str = '';
	for i in range(8):
		my_str += chr(random.randint(48, 122))
	return my_str
	
def  password_salt(passwd, salt = None):
	 if salt is None:
	      salt = random_password()
         hashed_password = hashlib.sha256( passwd+ salt ).digest()
	 return (salt, hashed_password)

def  password_(passwd):
	 salt = random_password()
         hashed_password = hashlib.sha256( passwd+ salt ).digest()
	 return (salt, hashed_password)

def activation_hash():
	my_rand = random_password()
	return password_salt(my_rand)[1]
	
def get_url(title):
	 title_words =  title.lower().split()
	 return  "_".join(title_words[:20])
	 
	 

def generate_password_and_salt():
    password = random_password()
    salt, hashed_password = password_salt(password)
    return (password, salt, hashed_password)
	
token = str(hashlib.sha256( random_password()).hexdigest())

#print token


def generate_url(surname, title):
    coo = "/".join(get_current_date_time().split(" ")[0].split("-"))
    url = get_url(title)
    return "/".join([coo, surname, url])
    
#print generate_url("foo", "Here we go")

#poot =  get_url("Here we go")
#print poot


	
