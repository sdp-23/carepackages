from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.conf import settings
from django.template import Template


# Create your views here.
def home(request):

	t = Template(open(settings.BASE_DIR + "/templates/index.t").read())
	return HttpResponse(t.render({}))
