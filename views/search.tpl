<html>
<head>
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">
%include header.tpl my_test=my_test
%if  type(rows) is dict:
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
<tr>
%for col in row:
<td>{{col['entry']}}</td>
%end
</tr>
%end
</table>
%else:
rows
%end
</div>
</body>
</html>