from django.db import models
from django.contrib.postgres.fields import ArrayField

class Libraries(models.Model):
    username = models.CharField(max_length=255, blank=False)
    password = models.TextField(blank=False)
    books = models.TextField(blank=True)
    price_of_books = models.IntegerField()
    budget = models.IntegerField()
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username