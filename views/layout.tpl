<html>
<head>
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">
%include header.tpl my_test=my_test
%include left.tpl 
%include center.tpl
%include right.tpl  my_test=my_test
%include footer.tpl
</div>
</body>
</html>