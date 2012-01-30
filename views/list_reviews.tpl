%import datetime

%include header.tpl my_top=1, token = 0
<p>The open items are as follows:</p>
%if reviews :
%if len(reviews) == 6:
%areviews = reviews[:5]
%else :
%areviews = reviews
%end
%for review in areviews :
<div>
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
<a  href = "/reviews/pages?start={{previous_point}}"> Previous </a></li> 
%else :
Previous </li> 
%end
<li>
%if len(reviews) == 6:
%start_point = start_point + 5
<a  href = "/reviews/pages?start={{start_point}}"> Next</a></li> 
%else :
Next </li></ul>
%end
%else :
We have nothing for your search
%end
</div>
%include footer.tpl my_bottom=1
