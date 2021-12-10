from django.db import models
from django.urls import reverse

# Create your models here.

class Palabras(models.Model):
    url = models.CharField(max_length=99999,default="https://es.wikipedia.org/")
    texto = models.CharField(max_length=9999999,default="")
    def __str__(self):
        return self.url
    
    def get_absolute_url(self):
        return reverse('count-detail', kwargs={'pk': self.pk})