%import datetime
<html>
<head>
<title>No title</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">
<p>The open items are as follows:</p>
%if reviews :
%if len(reviews) == 6:
%areviews = reviews[:5]
%areviews = areviews[::-1]
%else :
%areviews = reviews
%end
%for review in areviews :
<div>
<h4>{{review["title"]}}</h4>
<p>{{review["entry"][:40]}}</p>
<a href = "/reviews/{{review["id"]}}">...more</a>
<a href = "/users/{{review["user_id"]}}">{{review["username"]}}</a> 
<p>posted {{review["updated_time"].strftime("%B %d '%y at %H:%M")}}</p>
</div>
%end
<ul><li> 
%if  start_point > 5:
%previous_point = start_point - 5
<a  href = "/reviews/users?id={{review["user_id"]}}&start={{previous_point}}"> Previous </a></li> 
%else :
Previous </li> 
%end
<li>
%if len(reviews) == 6:
%start_point = start_point + 5
<a  href = "/reviews/users?id={{review["user_id"]}}&start={{start_point}}"> Next</a></li> 
%else :
Next </li>
%end
%else :
We have nothing for your search
%end
</div>
</body>
</html>