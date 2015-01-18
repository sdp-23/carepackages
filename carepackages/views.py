from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.conf import settings
from django.template import Template
from carepackages.models import User


# Create your views here.
def user_exists(request):
	user_id = request.GET.get("id")
	if (len(User.objects.filter(f_id = user_id)) > 0):
		ret = True
	else:
		ret = False
	return HttpResponse(str(ret))



