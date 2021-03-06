from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
import carepackages.views
import webpages.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #API urls
    url(r'^api/', include('carepackages.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #Facebook urls
    (r'^facebook/', include('django_facebook.urls')),
	(r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^', include('webpages.urls')),
) +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
