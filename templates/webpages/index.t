<link href="{{ STATIC_URL }}django_facebook/css/facebook.css" type="text/css" rel="stylesheet" media="all" />
{% include 'django_facebook/_facebook_js.html' %}

<form action="{% url 'facebook_connect' %}?facebook_login=1" method="post"> {% csrf_token %}
    <input type="hidden" value="/login" name="next" />
    <input type="hidden" value="/login" name="connect_next" />
    <input type="hidden" value="/login" name="register_next" />
    <input type="hidden" value="/" name="error_next" />
    {% csrf_token %}
    <input onclick="F.connect(this.parentNode); return false;" type="image" src="{{ STATIC_URL }}django_facebook/images/facebook_login.png" />
</form>

