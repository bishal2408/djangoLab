from django.db import models

# Create your models here.
class Agent(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    experienceInYears = models.IntegerField(default=0)
    rating = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property/%Y/%m/%d/', null=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
