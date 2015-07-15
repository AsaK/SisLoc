#-*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=512)
    type = models.CharField(max_length=1)
    creation_date = models.DateTimeField()


class Customers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    type = models.CharField(max_length=1)
    enabled = models.CharField(max_length=1)
    creation_date = models.DateTimeField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)
    type = models.CharField(max_length=1)
    creation_date = models.DateTimeField()


class Features(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField()


class Booking(models.Model):
    date_init = models.DateTimeField()
    date_final = models.DateTimeField()
    customer = models.ForeignKey(Customers)
    user = models.ForeignKey(Users)
    features = models.ManyToManyField(Features)
    creation_date = models.DateTimeField()
