from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.conf import settings
from django.template import Template

BASE_DIR = settings.BASE_DIR

# Create your views here.
def home(request):
	r = Template(open(BASE_DIR + "/assets/index.t").read())
	return r.render()

def login(request):
	return HttpResponse(str(request.POST))

