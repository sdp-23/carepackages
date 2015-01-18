from django.conf.urls import patterns, url

import webpages.views as webpages_views

urlpatterns = patterns('',
	url(r'login$', webpages_views.login, name='login_page'),
    url(r'$', webpages_views.home, name='index'),
)