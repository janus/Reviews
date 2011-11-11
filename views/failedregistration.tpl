<html>
<head>
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">
%include header.tpl my_test=my_test
<div>{{username}} , {{error_message}}</div>
<p>A mail is sent to your box, it has activation link.</p>
</div>
</body>
</html>








