from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^login$', carepackages.views.login, name='index'),
)