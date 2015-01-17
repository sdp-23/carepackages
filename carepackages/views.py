from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json

# Create your views here.
def display(request):
	return HttpResponse(json.dumps(str({"Status": "Success"}))[1:-1])
