from django.conf.urls import patterns, url

from carepackages import views

urlpatterns = patterns('',
    url(r'^sample$', views.home, name='index'),
)