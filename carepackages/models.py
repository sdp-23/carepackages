from django.db import models

# Create your models here.
class care_package(models.Model):
	name = models.CharField(max_length = 150)
	price = models.DecimalField(max_digits = 10, decimal_plaes = 2)
	store_name = models.CharField(max_length = 150)
	ups = models.IntegerField()
	downs = models.IntegerField()
	image_link = models.CharField(max_length = 250)


class item(models.Model):
	name = models.CharField(max_length = 150)
	price = models.DecimalField(max_digits = 10, decimal_plaes = 2)
	image_link = models.CharField(max_length = 250)

class user(models.Model):
	f_id = models.CharField(max_length = 50)
	stripe_user = models.CharField(max_length = 50)

