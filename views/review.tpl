%import datetime
%include header.tpl my_top=1 , token = 0
<div>
<h4>{{review["title"]}}</h4>
<p>{{review["entry"][:40]}}</p>
<a href = "/users/{{review["user_id"]}}">{{review["username"]}}</a> 
<p>posted {{review["updated_time"].strftime("%B %d '%y at %H:%M")}}</p>
</div>
<table border="1">
%if comments:
%for comment in comments:
<tr>
<td>{{comment["message" ]}} posted {{comment["created_time"].strftime("%B %d '%y at %H:%M")}} by {{comment["username"]}}</td>
</tr>
%end
%else:
Bye
%end
</table>
%include footer.tpl my_bottom=1
