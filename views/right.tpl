<div id = "right">
<!-- <div id="rregister"> */ -->
%if not my_test:
   <div id="right-up">
   <form id="register" method = "POST" action ="/register">

   <fieldset>
   <legend>Please create an account here</legend>
   <div class="form_row">
   <label   id="spec"   for="screen_name">Username:</label>
   <input type="text" name="username" id="Username"   value="" size="12">  
     </div>
    <div class="form_row">
   <label  id="spec" for="email">Email:</label>
   <input type="text" name="email" id="Email"   value=""  size="12">  
	</div> 
	<div class="form_row">
	<label  id="spec" for="password">Password:</label>
	<input type="password" name="password"  id="Passwd" size="12">    

	</div> 
	<div class="form_row">
	<label   id="spec"   for="password">Confirm Password:</label>
	<input type="password" name="conpassword"  id="Passwd" size="12">    
	</div> 
	<div class="form_row">
	<input type="submit" class="gsubmit" name="signIn" id="signIn" value="Register Now!" background="yellow">
	</div>
	</fieldset>
	</form>
	</div>
%else:
     <div id="search">
      <form id="login" method="GET" action="/search">
      <input type="text" name="asearch" id="mysearch" size="15"  value="" >  
      <input type="submit" name="submit" class="submit" id="signIn" value="Search"  >
      </form>
      </div>
%end

       <div id="right-down">
	<h3>Latest  Reviews</h3>

	<div class="list-text">The world of games without fire:by juke</div>

  <hr/>
      <div class="list-text" id="onelove">The home of games without fire:by puke</div>
      <div class="list-text">The hill of games without fire:by fuke</div>
      <div class="list-text">The citycenter of games without fire:by ruke</div>
      <div class="list-text">The new jersey without newness of games without fire:by jmuke</div>
      <div class="list-text">Boon chagger man, by oggo </div>

       <div class="list-text">Coon chagger man, by moggo </div>
        <div class="list-text">Xoon Whagger man, by figo </div>
    

</div>

</div>