<html>
<head>
<title>{{title or 'No title'}}</title>
<link rel="stylesheet" type="text/css" href="views/style.css">
</head>
<body>
<div id="pagewrap">
%include header.tpl my_test=my_test
%if cond == 1:
<div>{{username}} , {{mysuccess}}</div>
A mail is sent to your box, it has activation link.
%end
%if cond == 2:
<div>{{username}} , {{mysuccess}}</div>
<p>A mail is sent to your box, it has activation link.</p>
%end
</div>
</body>
</html>