from django.db import models


class Admin_list(models.Model):
    user_name=models.CharField(max_length=255)
    passcode=models.CharField(max_length=255)

    def __str__(self):
        return self.user_name


class Products(models.Model):
    productname=models.CharField(max_length=1000,default='')
    capacity=models.CharField(max_length=1000,default='')
    workingpressure=models.CharField(max_length=1000,default='')
    fuel=models.CharField(max_length=1000,default='')
    model_series=models.CharField(max_length=1000,default='')
    product_image=models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.productname
