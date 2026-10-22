from django.db import models

# Create your models here.

class ProductDb(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    description =models.TextField(null=True, blank=True)