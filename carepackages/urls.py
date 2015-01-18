from django.conf.urls import patterns, url
import carepackages.views as carepackages_views

urlpatterns = patterns('',
    url(r'exists', carepackages_views.user_exists, name='index'),
)
