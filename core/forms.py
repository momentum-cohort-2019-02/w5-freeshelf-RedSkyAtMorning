from django import forms
from django.forms import ModelForm
from core.models import Bead, Matron, Necklace, Bowl

class AddOrShowBead(forms.ModelForm):
    class Meta:
        model = Bead
        fields = ['name', 'description', 'author']

