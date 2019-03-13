from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
import uuid

# Create your models here.
class Bead(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)

    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('bead_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name

class Bowl(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)

    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('bowl_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name

class Necklace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)

    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('necklace_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name

class Matron(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)

    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('bead_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name