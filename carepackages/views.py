from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.conf import settings


# Create your views here.
def display(request):
	return HttpResponse(json.dumps(str({"ROOT": settings.STATIC_ROOT, 
										"URL": settings.STATIC_URL
	}))[1:-1])
