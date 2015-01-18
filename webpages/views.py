from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.conf import settings
from django.template import Template, Context


# Create your views here.
def home(request):

	t = Template(open(settings.BASE_DIR + "/templates/webpages/index.t").read())
	return HttpResponse(t.render(Context({"STATIC_URL": settings.STATIC_URL})))
