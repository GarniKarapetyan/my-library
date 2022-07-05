from django.db import models
from django.contrib.postgres.fields import ArrayField

class Libraries(models.Model):
    username = models.CharField(max_length=255, blank=False)
    password = models.TextField(blank=False)
    books = ArrayField(models.CharField(max_length=150, blank=True),size=150)
    price_of_books = models.IntegerField()
    budget = models.IntegerField()
    time_update = models.DateTimeField(auto_now=True)