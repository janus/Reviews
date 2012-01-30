%import sys
% dir = "/home/rmicro/myPython/Reviews/mydatamodel/config/"
% sys.path.append(dir)
%import dconfig
%include header.tpl my_top=1

<h2>Login here!</h2>
%if cond:
<div id="error"> <p>{{error_message}}</p></div>
%end
<form method="POST" action = "/login">
<fieldset>
<p>
<label for="review_email">Email</label>
<input type="text" id="review_email" name="email" value="" maxlength="{{dconfig.email_maxlength}}" />
</p>
<p>
<label for="review_password">Password</label>
<input type="password" id="review_password" name="password" value="" maxlength="{{dconfig.password_maxlength}}" />
</p>
<p>
<input type="hidden" name="form_token" value="{{token}}" />
<input type="submit" value="&rarr;  Login " />
</p>
</fieldset>
</form>

%include footer.tpl
