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
    expiry = request.POST.get("expiry").replace('/', '')
    exp_month = int(expiry)/100
    exp_year = int(expiry) - exp_month*100 + 2000
    #try:
    stripe.api_key = "sk_test_FdEFjYayNgCmvuaeUc0IAr7X"
    s=stripe.Customer.create(
        description="Customer for test@example.com",
        card={'number': request.POST.get('cc_num'),
            'exp_month': exp_month,
            'exp_year': exp_year,
            'cvc': request.POST.get('cvc'),
            'name': request.POST.get('user_name'),
        }
    )
    u = User(f_id = str(request.POST.get("fb_id")), stripe_user = str(s.id))
    u.save()
    #except stripe.CardError, ce: 
    #    return HttpResponse("Failure")

    return HttpResponse("Success")

    

