from django.db import models
import datetime
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    name = models.CharField(max_length=100)
    civilid = models.IntegerField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    nationality = models.CharField(max_length=100,null=True,blank=True)
    work_tel = models.IntegerField(null=True,blank=True)
    home_tel = models.IntegerField(null=True,blank=True)
    mobile = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    notes = models.CharField(max_length=250,null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True,blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Billable(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Visit(models.Model):
    PAYMENT_CHOICES = (
    ('C', 'Cash'),
    ('K', 'K-NET'),
    ('M', 'M-NET'),
    ('I', 'Insurance')
    )
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField(auto_now=False,auto_now_add=False)
    time = models.TimeField(auto_now=False,auto_now_add=False)
    payment = models.CharField(max_length=1, choices=PAYMENT_CHOICES, null=True,blank=True)
    fee = models.IntegerField(null=True,blank=True)
    notes = models.CharField(max_length=250,null=True,blank=True)
    billables = models.ManyToManyField(Billable)
    def calc(self):
        price = 0
        for item in self.billables.all():
            price = price + item.price
            print(price)
        self.fee = price
        self.save()
    def __str__(self):
        return self.patient.name 


def get_full_price(instance, *args, **kwargs):
    instance.calc()

m2m_changed.connect(get_full_price, sender=Visit.billables.through)
