from django.db import models
from django.utils import timezone

class reg_user(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    address=models.CharField(max_length=300)

class crop_table(models.Model):
    u_id=models.CharField(max_length=150)
    N=models.CharField(max_length=200)
    P=models.CharField(max_length=150)
    K=models.CharField(max_length=150)
    temperature=models.CharField(max_length=150)
    humidity=models.CharField(max_length=150)
    ph=models.CharField(max_length=150)
    rainfall=models.CharField(max_length=150)
    result=models.CharField(max_length=150)

class ftlzr_table(models.Model):
    u_id=models.CharField(max_length=150)
    N=models.CharField(max_length=200)
    P=models.CharField(max_length=150)
    K=models.CharField(max_length=150)
    crop_type=models.CharField(max_length=150)
    result=models.CharField(max_length=150)

class plant_disease(models.Model):
    u_id=models.CharField(max_length=150)
    file=models.FileField(max_length=200)
    label=models.CharField(max_length=250)
    remedies=models.CharField(max_length=1000)
    pesticides=models.CharField(max_length=250)

class product(models.Model):
    product_type=models.CharField(max_length=150)
    product_name=models.CharField(max_length=100)
    crop_type=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    image=models.CharField(max_length=500)

class purchase(models.Model):
    uid=models.CharField(max_length=100)
    #name=models.CharField(max_length=100)
    pr_id=models.CharField(max_length=100)
    #product_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    rate=models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    cardtype=models.CharField(max_length=100)
    cardname=models.CharField(max_length=100)
    cardnumber=models.CharField(max_length=100)
    cvv=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    #phone=models.CharField(max_length=100)