<html>
<head>
%title = "Maamariga"
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="/views/style.css">
  <script type="text/javascript" src="/views/jscripts/tiny_mce/tiny_mce.js"></script>
   <script type="text/javascript" src="/views/revieweditor.js"></script>
</head>
<body>
<div id="pagewrap">
<div id = "header">
<h3>&#8230;and all looks good, from a&#160;distance.</h3>
<div id="my-title"><h3><blockquote><span class="T_before_o">M</span>aamariga</blockquote></h3><p id="tdsgin">A review site with a difference</p></div>

      <div id="llogin">
%if not my_top:
      <form id="login" method="POST" action="/login">
      <label>
      <strong class="email-label">Email</strong> <input type="text" name="email" id="Email" size="7"  value="" />  
      </label>
      <label>
      <strong class="passwd-label">Password</strong><input type="password" name="password" size="7" id="Passwd" />    
      </label>
      <input type="hidden" name="form_token" value="{{token}}" />
      <input type="submit" class="g-button g-button-submit" name="signIn" id="signIn" value="Sign in" background="yellow" size="5" />
      </form>
      <div><a href ="/reset/password">Can't access your account?</a></div>  
      </div>
%else:
%if type(my_top) == str:
       <p>Welcome {{my_top}}</p>
	<form method="GET" action = "/logout">
	<input type="submit" name="submit" value="log Out!" /></form></div>
%else:
</div>
%end
%end
</div>
 <div id="content">
 <ul id="nav">
 <li><a href="/index">Home</a></li>
 <li><a href="/reviews">Reviews</a></li>
 <li><a href="/review/create">Create a Review</a></li>
 <li> <form id="search" method="GET" action="/search">
      <input type="text" name="asearch" id="mysearch" size="20"  value="" />  
      <input type="submit" name="submit" class="submit" id="buttonsearch" value="Search" />
      </form></li>
 </ul>
 </div>

