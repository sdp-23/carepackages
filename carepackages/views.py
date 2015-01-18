from django.shortcuts import render
from django.http import HttpResponse
import simplejson as json
from django.conf import settings
from django.template import Template
from carepackages.models import User
import stripe


# Create your views here.
def user_exists(request):
	user_id = request.GET.get("id")
	if (len(User.objects.filter(f_id = user_id)) > 0):
		ret = True
	else:
		ret = False
	return HttpResponse(str(ret))

def create_user(request):
    try:
        stripe.api_key = "sk_test_FdEFjYayNgCmvuaeUc0IAr7X"
        s=stripe.Customer.create(
            description="Customer for test@example.com",
            card={'number': request.POST.get('number'),
                'exp_month': request.POST.get('exp_month'),
                'exp_year': request.POST.get('exp_year'),
                'cvc': request.POST.get('cvc'),
                'name': request.POST.get('name'),
            }
        )
    except stripe.CardError, ce: 
        return HttpResponse("Failure")

    return HttpResponse(str(s))

