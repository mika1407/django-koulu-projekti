from django.db import models

# Create your models here.
class Supplier(models.Model):
    companyname = models.CharField(max_length=50, default='lakufirma')
    contactname = models.CharField(max_length=50, default='tommi')
    address = models.CharField(max_length=100, default='tie 5')
    phone = models.CharField(max_length=20, default= '234324876')
    email = models.CharField(max_length=50, default= 'timo.tilli@tilli.com')
    country = models.CharField(max_length=20, default= 'Finland')

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.IntegerField(default = 3)
    unitsinstock = models.IntegerField(default= 3)
    companyname = models.CharField(max_length= 50, default= 'lakufirma')