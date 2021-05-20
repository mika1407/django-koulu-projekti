from django.db import models

# Create your models here.
class Supplier(models.Model):
    companyname = models.CharField(max_length=50, default='lakufirma')
    contactname = models.CharField(max_length=50, default='tommi')
    address = models.CharField(max_length=100, default='tie 5')
    phone = models.CharField(max_length=20, default= '234324876')
    email = models.CharField(max_length=50, default= 'timo.tilli@tilli.com')
    country = models.CharField(max_length=20, default= 'Finland')

    # class Meta:
    #     ordering =['companyname']

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default= 3)
    companyname = models.CharField(max_length= 50, default= 'lakufirma')
    # supplier = models.ForeignKey(Supplier, on_)