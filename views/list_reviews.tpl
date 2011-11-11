<html>
<head>
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">
%include header.tpl my_test=my_test
<p>The open items are as follows:</p>
<table border="1">
%for review in reviews:
<tr>
<td>{{review['message']}}</td>
</tr>
%end
</table>
</div>
</body>
</html>