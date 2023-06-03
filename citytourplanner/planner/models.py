from django.db import models
from django.utils import timezone

# Create your models here.
class Search(models.Model):
    city = models.CharField(max_length=100, null=True)
    documented = models.CharField(max_length=100, null=True)
    tourism_filters = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.city