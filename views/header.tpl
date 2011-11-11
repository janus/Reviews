<div id = "header">
<h3>&#8230;and all looks good, from a&#160;distance.</h3>
<div id="my-title"><h3><blockquote><span class="T_before_o">M</span>aamariga</blockquote></h3><p id="tdsgin">A review site with a difference</p></div>

      <div id="llogin">
%if not my_test:
      <form id="login" method="POST" action="/login">
      <label>
      <strong class="email-label">Email</strong> <input type="text" name="email" id="Email" size="7"  value="" >  
      </label>
      <label>
      <strong class="passwd-label">Password</strong><input type="password" name="password" size="7" id="Passwd">    
      </label>
      <input type="submit" class="g-button g-button-submit" name="signIn" id="signIn" value="Sign in" background="yellow" size="5">
      </form>
      <div><a href ="/hoo">Can't access your account?</a></div>  
      </div>
%else:
%if type(my_test) == str:
       <p>Welcome {{my_test}}</p>
	<form method="GET" action = "/logout">
	<input type="submit" name="submit" value="log Out!" /></form></div>
%else:
</div>
%end
%end
 </div>
