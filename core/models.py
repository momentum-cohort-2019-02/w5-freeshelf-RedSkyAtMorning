from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.contrib.auth import get_user_model
import uuid

# Create your models here.
User = get_user_model()


class Matron(models.Model):
    userid = models.OneToOneField(User, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)
    linkedin = models.URLField(max_length=200,null=True, blank=True)
    last_rating = models.DecimalField(max_digits=6, decimal_places=4,null=True, blank=True)
    last_rating_on = models.DateField(auto_now_add=True,null=True, blank=True)
    is_crone = models.BooleanField(default=False)
    #tracker

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

    collecting = models.ManyToManyField(
        to='Bead', related_name='bowl_id', through='Resemblance')
    #tracker

    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('bowl_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name

class Bead(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)
    author = models.CharField(max_length=100,null=True, blank=True)
    citationURL = models.URLField(max_length=200,null=True, blank=True)
    name_slug = models.SlugField(max_length=100,null=True, blank=True)
    first_sponsor = models.ForeignKey(Matron,on_delete=models.PROTECT, null=True, blank=True)
    
    collected_by = models.ManyToManyField(
        to='Bowl', related_name='bead_id', through='Resemblance')
    
    strung_with = models.ManyToManyField(
        to='Necklace', related_name='bead_id', through='Membership')
    #tracker

    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('bead_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name

class Necklace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)

    stringing = models.ManyToManyField(
        to='Bead', related_name='necklace_id', through='Membership')
    #tracker

    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('necklace_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name






class Status(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)
    order_by_help = models.PositiveSmallIntegerField(null=True, blank=True)
    #tracker

    class Meta:
        ordering = ['order_by_help',]

    def __str__(self):
        return self.name

class Resemblance(models.Model):
    bead_id = models.ForeignKey('Bead', on_delete=models.PROTECT, null=True, blank=True)
    bowl_id = models.ForeignKey('Bowl', on_delete=models.PROTECT, null=True, blank=True)
    #tracker

class Membership(models.Model):
    bead_id = models.ForeignKey('Bead', on_delete=models.PROTECT, null=True, blank=True)
    necklace_id = models.ForeignKey('Necklace', on_delete=models.PROTECT, null=True, blank=True)
    #tracker