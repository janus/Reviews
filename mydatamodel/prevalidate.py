from config import dconfig
from dvalidation import validate


def validate_email(my_email):
	return validate(my_email, item_reg = dconfig.email_pattern)
	
def validate_password(password):
	 return validate(password, min_length = dconfig.password_minlength,max_length = dconfig.password_maxlength, item_reg =dconfig.password_pattern)
	 
def validate_name(name):
      return validate(name, min_length = dconfig.name_minlength,max_length = dconfig.name_maxlength, item_reg = dconfig.name_pattern, casetype = True)

def validate_username(username):
	return validate(username, min_length = dconfig.username_minlength, max_length = dconfig.username_maxlength, item_reg = dconfig.username_pattern, casetype = True)
        
def validate_title(heading):
       return validate(heading, min_length = dconfig.title_minlength, max_length = dconfig.title_maxlength, item_reg = dconfig.title_pattern, casetype = True )
       
def validate_voting(vote):
        return validate(vote, item_reg = dconfig.voting_pattern)
       
def validate_entry(my_text):
	return validate(my_text, min_length = dconfig.review_minlength,  item_reg = dconfig.review_pattern)	
	
def validate_time(my_time):
        return validate(my_time, item_reg = dconfig.time_pattern)
	
def validate_streetaddress(streetaddress):
	return validate(streetaddress, item_reg = dconfig.streetaddress_pattern)

def validate_message(message):
      return validate(message, min_length = dconfig.message_minlength,max_length = dconfig.message_maxlength, item_reg = dconfig.message_pattern)

hoo = "root" if validate_time("2011-09-20 00:24:5") else "loop"
print hoo