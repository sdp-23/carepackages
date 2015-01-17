from django.conf.urls import patterns, url

from webpages import views

urlpatterns = patterns('',
    url(r'^$', views.display, name='index'),
)