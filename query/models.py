from django.db import models
from property.models import Property

# Create your models here.
class Query(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)
    message = models.TextField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    def __str__(self):
        self.title
