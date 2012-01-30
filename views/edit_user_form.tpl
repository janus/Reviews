%import sys
% dir = "/home/rmicro/myPython/Reviews/mydatamodel/config/"
% sys.path.append(dir)
%import dconfig
<html>
<head>
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">
%include header.tpl my_top=my_top, token = 0
<h2>Register here!</h2>
%if not cond:
<div id="error"> <p>{{error_message}}</p>
%end
<form action="/register" method="post">
<fieldset>
<p>
<label for="review_email">Email</label>
<input type="text" id="review_email" name="email" value="{{email}}" maxlength="{{dconfig.email_maxlength}}" />
</p>
<p>
<label for="review_currentpassword">Current Password</label>
<input type="password" id="review_password" name="currentpassword" value="" maxlength="{{dconfig.password_maxlength}}" />
</p>
<p>
<label for="review_newpassword">New Password</label>
<input type="password" id="review_password" name="newpassword" value="" maxlength="{{dconfig.password_maxlength}}" />
</p>
<p>
<label for="review_confirmpassword">Confirm Password</label>
<input type="password" id="review_password" name="conpassword" value="" maxlength="{{dconfig.password_maxlength}}" />
</p>
<p>
<input type="hidden" name="form_token" value="{{token}}" />
<input type="submit" value="&rarr; Login" />
</p>
</fieldset>
</form>
</div>
%include footer.tpl my_bottom=my_bottom
</body>
</html>

