<html>
<head>
	<link rel="stylesheet" type="text/css" href="/static/carepackage.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
</head>
<script>
var login = function(){
	FB.login(function(response) {
   		if (response.authResponse) {
     		console.log('Welcome!  Fetching your information.... ');
     		FB.api('/me', function(response) {
       		console.log('Good to see you, ' + response.name + '.');
     	});
   		} else {
     		console.log('User cancelled login or did not fully authorize.');
   		}
 	});
}
 </script>
<body>
	<div id="landing">
		<div class="spacer"></div>
		<div id="logo"></div>
		<h1 class="logotype" id="landinglogotype">CAREPACKAGE.IO</h1>
		<p id="slogan">Description of what Carepackage.io does, why it's so nice etc.</p>
		<div class="landingdivider"></div>
		<div id="fbsignin" onclick="login()"><div class="fblogobg"></div><a href="#">Sign in with Facebook</a></div></form>
</div>


</body>
</html>