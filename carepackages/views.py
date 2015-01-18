from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.conf import settings
from django.template import Template

BASE_DIR = settings.BASE_DIR

# Create your views here.
<<<<<<< HEAD
def login(request):
	r = Template(open(BASE_DIR + "/assets/index.t").read())
	return r.render()


=======
def display(request):
	return HttpResponse(json.dumps(str({"ROOT": settings.STATIC_ROOT, 
										"URL": settings.STATIC_URL
	}))[1:-1])


def process_card_data(request):
	cc
	date
	cv
	name

	create_customer(cc, date, cv, name)

	
>>>>>>> templates
