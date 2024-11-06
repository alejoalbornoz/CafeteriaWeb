from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True) #nombre clave
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name