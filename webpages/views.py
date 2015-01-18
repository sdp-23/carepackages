from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.conf import settings
from django.template import Template, Context
from django.template import RequestContext
from django.core.context_processors import csrf


# Create your views here.
def home(request):
	t = Template(open(settings.BASE_DIR + "/templates/webpages/index.t").read())
	return HttpResponse(t.render(RequestContext(request)))

def login(request):
	t = Template(open(settings.BASE_DIR + "/templates/webpages/ccentry.html").read())
	return HttpResponse(t.render(RequestContext(request)))

def display(request):
	t = Template(open(settings.BASE_DIR + "/templates/webpages/ccentry.html").read())
	return HttpResponse(t.render(RequestContext(request)))