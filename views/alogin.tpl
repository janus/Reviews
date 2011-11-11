<html>
<head>
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">

%include header.tpl my_test=my_test
<div  id="center" >
<p>Your login failed,please again!</p>
<form method="POST" action = "/login">
Email:<input name="name" type="text" /><br />
Password:<input name="password" type="password" /><br />
<input type = "submit" name="submit" value="login!"/> 
</form>
</div>

%include footer.tpl
</div>
</body>
</html>
