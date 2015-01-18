<html>
<head>
	<link rel="stylesheet" type="text/css" href="/static/carepackage.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
</head>

<body>
	<div id="landing">
		<div class="spacer"></div>
		<div id="logo"></div>
		<h1 class="logotype" id="landinglogotype">CAREPACKAGE.IO</h1>
		<p id="slogan">Description of what Carepackage.io does, why it's so nice etc.</p>
		<div class="landingdivider"></div>

<link href="{{ STATIC_URL }}django_facebook/css/facebook.css" type="text/css" rel="stylesheet" media="all" />
{% include 'django_facebook/_facebook_js.html' %}

<form action="{% url 'facebook_connect' %}?facebook_login=1" method="post"> {% csrf_token %}
    <input type="hidden" value="/login" name="next" />
    <input type="hidden" value="/error" name="error_next" />
    {% csrf_token %}
	<div id="fbsignin" onclick="F.connect(this.parentNode); return false;"><div class="fblogobg"></div><a href="#">Sign in with Facebook</a></div></form>

</div>


</body>
</html>