<link href="{{ STATIC_URL }}django_facebook/css/facebook.css" type="text/css" rel="stylesheet" media="all" />
{% include 'django_facebook/_facebook_js.html' %}

<form action="{% url 'facebook_connect' %}?facebook_login=1" method="post">
    <input type="hidden" value="{{ request.path }}" name="next" />
    <input type="hidden" value="{{ request.path }}" name="register_next" />
    <input type="hidden" value="{{ request.path }}" name="error_next" />
    {% csrf_token %}
    <input onclick="F.connect(this.parentNode); return false;" type="image" src="{{ STATIC_URL }}django_facebook/images/facebook_login.png" />
</form>

