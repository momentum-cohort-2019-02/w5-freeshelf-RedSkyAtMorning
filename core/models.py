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
   
    dressing_with = models.ManyToManyField(
        to='Dress', related_name='matron_id', through='Dressing')
    
    outfitting_with = models.ManyToManyField(
        to='Shoe', related_name='matron_id', through='Outfitting')

    drumming_with = models.ManyToManyField(
        to='Beat', related_name='matron_id', through='Drumming')

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

    collecting_with = models.ManyToManyField(
        to='Bead', related_name='bowl_id', through = 'Collecting')
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
    
    collected_to = models.ManyToManyField(
        to='Bowl', related_name='bead_id', through='Collecting')
    
    strung_to = models.ManyToManyField(
        to='Necklace', related_name='bead_id', through='Stringing')
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

    stringing_with = models.ManyToManyField(
        to='Bead', related_name='necklace_id', through='Stringing')
    #tracker

    
    class Meta:
        ordering = ['name',]

    def get_absolute_url(self):
        return reverse('necklace_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name

class Dress(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField(max_length=1000,null=True, blank=True)
    order_by_help = models.PositiveSmallIntegerField(null=True, blank=True)
    dressed_on = models.ManyToManyField(
        to='Matron', related_name='dress_id', through='Dressing')
    #tracker

    class Meta:
        ordering = ['name',]

    class Meta:
        ordering = ['order_by_help',]

    def get_absolute_url(self):
        return reverse('dress_detail', args=[str(self.pk)])


    def __str__(self):
        return self.name

class Shoe(models.Model):
    keyword = models.CharField(max_length=100)
    shoe_boolean = models.BooleanField
    more = models.TextField(max_length=1000,null=True, blank=True)
    shoeURL = models.URLField(max_length=200,null=True, blank=True)
    
    shoed_on = models.ManyToManyField(
        to='Dressing', related_name='shoe_id', through='Outfitting')
    #tracker

    class Meta:
        ordering = ['keyword',]

    def get_absolute_url(self):
        return reverse('skin_detail', args=[str(self.pk)])

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

class Collecting(models.Model):
    bead_id = models.ForeignKey('Bead', on_delete=models.PROTECT, null=True, blank=True)
    bowl_id = models.ForeignKey('Bowl', on_delete=models.PROTECT, null=True, blank=True)
    #tracker

class Stringing(models.Model):
    bead_id = models.ForeignKey('Bead', on_delete=models.PROTECT, null=True, blank=True)
    necklace_id = models.ForeignKey('Necklace', on_delete=models.PROTECT, null=True, blank=True)
    #tracker

class Dressing(models.Model):
    dress_id = models.ForeignKey('Dress', on_delete=models.PROTECT, null=True, blank=True)
    matron_id = models.ForeignKey('Matron', on_delete=models.PROTECT, null=True, blank=True)
    #tracker

    dressed_with = models.ManyToManyField(
        to='Shoe', related_name='dressing_id', through='Outfitting')

class Outfitting(models.Model):
    shoe_id = models.ForeignKey('Shoe', on_delete=models.PROTECT, null=True, blank=True)
    dressing_id = models.ForeignKey('Dressing', on_delete=models.PROTECT, null=True, blank=True)
    matron_id = models.ForeignKey('Matron', on_delete=models.PROTECT, null=True, blank=True)
     
    #tracker

class Beat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True, blank=True)
    meeting_on = models.DateField(auto_now_add=True,null=True, blank=True)
    meeting_start_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    meeting_end_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    meeting_type  = models.CharField(max_length=100)
    meetupURL = models.URLField(max_length=200,null=True, blank=True)
    drummed_by = models.ManyToManyField(
        to='Beat', related_name='beat_id', through='Drumming')
    #tracker

    class Meta:
        ordering = ['-meeting_on',]

    def get_absolute_url(self):
        return reverse('bead_detail', args=[str(self.pk)])
        #That first argument is supposed to be the URL, not the view

    def __str__(self):
        return self.name

class Drumming(models.Model):
    beat_id = models.ForeignKey('Beat', on_delete=models.PROTECT, null=True, blank=True)
    matron_id = models.ForeignKey('Matron', on_delete=models.PROTECT, null=True, blank=True)
    #tracker