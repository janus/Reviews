<div id = "right">
%if not my_top:
   <div id="right-up"><p>Not a member? <a href="/register">  Register here</a></p></div>
%end
       <div id="right-down">
	<h3>Latest  Reviews</h3>
%reviews = reviews[::-1]
%reviews = reviews[:6]
%for review in reviews :
<div class="list-text"><a href="/reviews/{{review["id"]}} ">{{review["title"][:30]}}<a href = "/users/{{review["user_id"]}}">: by {{review["username"]}}</a> </div>"
%end
 </div>
</div>