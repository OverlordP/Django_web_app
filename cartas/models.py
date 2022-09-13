from django.db import models

# Create your models here.
class Cartas2(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    Url = models.URLField(blank=True)

class Cartas3(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    Url = models.URLField(blank=True)

