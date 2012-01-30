%import sys
% dir = "/home/rmicro/myPython/Reviews/mydatamodel/config/"
% sys.path.append(dir)
%import dconfig
%token = 0
%include header.tpl my_top=my_top , token = token
<h2>Register here!</h2>
%if cond:
<div id="error"> <p>{{error_message}}</p></div>
%end
<form action="/register" method="post">
<fieldset>
<p>
<label for="review_username">Username</label>
<input type="text" id="review_username" name="username" value="" maxlength="{{dconfig.username_maxlength}}" />
</p>
<p>
<label for="review_email">Email</label>
<input type="text" id="review_email" name="email" value="" maxlength="{{dconfig.email_maxlength}}" />
</p>
<p>
<label for="review_password">Password</label>
<input type="password" id="review_password" name="password" value="" maxlength="{{dconfig.password_maxlength}}" />
</p>
<p>
<label for="review_conpassword">Confirm Password</label>
<input type="password" id="review_conpassword" name="conpassword" value="" maxlength="{{dconfig.password_maxlength}}" />
</p>
<p>
<input type="hidden" name="form_token" value="{{token}}" />
<input type="submit" value="&rarr; Sign Up" />
</p>
</fieldset>
</form>
%include footer.tpl 


