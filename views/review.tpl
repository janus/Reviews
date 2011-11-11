<html>
<head>
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">
%include header.tpl my_test=my_test
{{review}}
<p>The open items are as follows:</p>
<table border="1">
%for comment in comments:
<tr>
<td>{{comment['message']}}</td>
</tr>
%end
</table>
</div>
</body>
</html>