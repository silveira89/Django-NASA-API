from django.db import models

# Create your models here.

class NasaJson(models.Model):
    date = models.CharField(max_length=20)
    explanation = models.TextField(max_length=2000)
    hdurl = models.CharField(max_length=200)
    mediaType = models.CharField(max_length=20)
    serviceVersion = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.title