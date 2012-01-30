%import sys
% dir = "/home/rmicro/myPython/Reviews/mydatamodel/config/"
% sys.path.append(dir)
%import dconfig
%include header.tpl my_top=1
<h2>{{message}}</h2>
<form method="POST" action = "/reset/password">
<fieldset>
<p>
<label for="review_email">Email</label>
<input type="text" id="review_email" name="email" value="" maxlength="{{dconfig.email_maxlength}}" />
</p>
<p>
<input type="submit" value="&rarr;  Send " />
</p>
</fieldset>
</form>

%include footer.tpl
