from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', webpages.views.display, name='index'),
)