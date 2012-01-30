import re


def validate(item, min_length = None, max_length = None, item_reg = None, casetype = None):
	if min_length is None:
		pass
	else:
	       if len(item) < min_length:
                     return False
	if max_length is None:
		pass
	else:
	       if len(item) > max_length:
                     return False  
	if item_reg is None:
		pass
	else:
		if casetype is None:
	              pattern = re.compile(item_reg)
	              return pattern.match(item)
		else:
	              pattern = re.compile(item_reg, re.IGNORECASE )
	              return pattern.match(item)     
	return True
	

       
#def validate_time(my_time)
