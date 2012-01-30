 %import sys
% dir = "/home/rmicro/myPython/Reviews/mydatamodel/config/"
% sys.path.append(dir)
%import dconfig
%token = 0
%include header.tpl my_top=my_top , token = token   
%include left.tpl 
<div id = "center">
<form id="login" method="POST" action="/review/create">
<div><label>Select Sector:</label><select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select></div>
    <div>
      <textarea cols="70" rows="40" id="articleContent" name="articleContent">
        &lt;h1&gt;Create a Review&lt;/h1&gt;
        &lt;p&gt;Your review here:&lt;/p&gt;
      </textarea>
<input type="hidden" name="user_id" value="{{user_id}}" />
      <input type="submit"  id = "postsubmit" value="Post"/>
    </div>
  </form>
  </div>
%include right.tpl  my_top=my_top, reviews=reviews
%include footer.tpl 
