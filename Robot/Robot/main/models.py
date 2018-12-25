from django.db import models

# Create your models here.


class Site(models.Model):
    url = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True, auto_now=True)
    status = models.IntegerField(null=True)