<html>
<head>
	<link rel="stylesheet" type="text/css" href="/static/carepackage.css">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
<script type="text/javascript" src="http://www.json.org/json2.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
<script>
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
      window.fbAsyncInit = function() {
        FB.init({
          appId      : '712828142168872',
          xfbml      : true,
          version    : 'v2.2'
        });
      };

      (function(d, s, id){
         var js, fjs = d.getElementsByTagName(s)[0];
         if (d.getElementById(id)) {return;}
         js = d.createElement(s); js.id = id;
         js.src = "//connect.facebook.net/en_US/sdk.js";
         fjs.parentNode.insertBefore(js, fjs);
       }(document, 'script', 'facebook-jssdk'));
    </script>
<script>
var login = function(){
	FB.login(function(response) {
   		if (response.authResponse) {
     		FB.api('/me', function(response) {
     			$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }}});
     			$.ajax({
    				type: "POST",
    				url: '/login',
    				data: response,
    				dataType: "json",
    				success: function(data, textStatus) {
    					console.log(data);
    					console.log(textStatus);
        				if (data.redirect) {
            				// data.redirect contains the string URL to redirect to
            				alert(data.redirect);
            				window.location.href = data.redirect;
        					}
        				else {
            				// data.form contains the HTML for the replacement form
        				}
    				}
				});
     	});
   		} else {
     		console.log('User cancelled login or did not fully authorize.');
   		}
 	});
}
 </script>
 </head>


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