from django.conf.urls import patterns, url
import carepackages.views as carepackages_views

urlpatterns = patterns('',
    url(r'^login$', views.login, name='index'),
    url(r'^login$', carepackages_views.login, name='index'),
)
