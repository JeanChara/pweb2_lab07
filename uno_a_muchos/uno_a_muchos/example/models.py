from django.db import models

# Create your models here.

class Simple(models.model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')

    def __str__(self):
        return self.url
class DateExample(models.Model):
    the_date = models.DateField()

class NullExample(models.Model):
    col = models.CharField(max_length=10, blank=True, null=True)