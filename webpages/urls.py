from django.conf.urls import patterns, url

import webpages.views as webpages_views

urlpatterns = patterns('',
	url(r'browse$', webpages_views.display, name='main_page'),
	url(r'register$', webpages_views.login, name='login_page'),
    url(r'$', webpages_views.home, name='index'),
)