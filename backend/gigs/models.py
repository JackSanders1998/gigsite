import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Gig(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    start_datetime = models.DateTimeField('gig starts')
    end_datetime = models.DateTimeField('gig ends')
    
    def __str__(self):
        return self.title
class User(models.Model):
    url = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    groups = models.CharField(max_length=120)

    def __str__(self):
        return self.username

class Group(models.Model):
    url = models.CharField(max_length=120)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name