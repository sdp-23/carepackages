from django.conf.urls import patterns, url

import webpages.views as webpages_views

urlpatterns = patterns('',
    url(r'^$', webpages_views.home, name='index'),
)