from django.conf.urls import patterns, url

import carepackages.views as carepackages_views

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^login$', carepackages_views.login, name='index'),
=======
<<<<<<< HEAD
    url(r'^login$', views.login, name='index'),
=======
    url(r'^login$', carepackages_views.login, name='index'),
>>>>>>> templates
>>>>>>> d354b9a3c21444802cf21f269d7fbdadc09978f5
)