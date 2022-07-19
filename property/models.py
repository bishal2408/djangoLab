from django.db import models

# Create your models here.
from agent.models import Agent


class Property(models.Model):
    title = models.CharField(max_length=255)
    shortDescription = models.CharField(max_length=255)
    longDescription = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    featured = models.BooleanField(default=True)
    status = models.CharField(max_length=255)
    kitchen = models.IntegerField(default=0)
    hall = models.IntegerField(default=0)
    bedroom = models.IntegerField(default=0)
    roadInFront = models.CharField(max_length=255)
    distanceFromHighway = models.IntegerField(default=0)
    garage = models.BooleanField(default=False)
    shutter = models.BooleanField(default=False)
    coverImage = models.ImageField(upload_to='property/%Y/%m/%d/', null=True)
    cardImage = models.ImageField(upload_to='property/%Y/%m/%d/', null=True)
    area = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null= True)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

