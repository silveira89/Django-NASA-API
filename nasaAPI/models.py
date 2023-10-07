from django.db import models

# Create your models here.

class NasaJson(models.Model):
    date = models.DateField()
    explanation = models.TextField(max_length=2000)
    hdurl = models.CharField(200)
    mediaType = models.CharField(20)
    serviceVersion = models.CharField(20)
    title = models.CharField(200)
    url = models.CharField(200)