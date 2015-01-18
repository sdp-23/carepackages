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
    expiry = request.GET.get("expiry").split("/")
    exp_month = expiry[0]
    exp_year = expiry[1]
    #try:
    stripe.api_key = "sk_test_FdEFjYayNgCmvuaeUc0IAr7X"
    s=stripe.Customer.create(
        description="Customer for test@example.com",
        card={'number': request.GET.get('cc_num'),
            'exp_month': exp_month,
            'exp_year': exp_year,
            'cvc': request.GET.get('cvc'),
            'name': request.GET.get('user_name'),
        }
    )
        u = User(request.GET.get("fb_id"), s["id"])
        u.save()
    #except stripe.CardError, ce: 
    #    return HttpResponse("Failure")

    return HttpResponse("Success")

