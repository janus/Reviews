
	//<!-- 
	//Browser Support Code
	function ajaxFunction(form){
	var ajaxRequest;  // The variable that makes Ajax possible!
	var continent = document.form.site.options[document.form.site.selectedIndex].value;	
	try{
	// Opera 8.0+, Firefox, Safari
	ajaxRequest = new XMLHttpRequest();
	} catch (e){
	// Internet Explorer Browsers
	try{
	ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
	} catch (e) {
	try{
	ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
	} catch (e){
	// Something went wrong
	alert("Your browser broke!");
	return false;
	}
	}
	}
	// Create a function that will receive data sent from the server
	ajaxRequest.onreadystatechange = function(){
	var ajaxDisplay = document.getElementById('ajaxDiv');
	ajaxDisplay.options.length  = 0;
	if(ajaxRequest.readyState == 4){
	var myresponse = ajaxRequest.responseText ;
	var responseData = eval( "(" + myresponse + ")" );
	for(var i = 0; i < responseData["foo"].length ; i++)
	{
	  
	try{
	ajaxDisplay.add(new Option(responseData["foo"][i], ""+' ' + i), null) //a
	}
	catch(e){ //in IE, try the below version instead of add()

	ajaxDisplay.add(new Option(responseData["foo"][i], ""+' ' + i)) 

	}
	}

	}
	}
	var queryString = "?continent=" + continent ;
	ajaxRequest.open("GET", "ajaxhome" + queryString, true);
	ajaxRequest.send(null); 
                   }

	//-->
	//</script>