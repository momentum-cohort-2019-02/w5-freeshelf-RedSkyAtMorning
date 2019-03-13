from django.shortcuts import render
from core.models import Bead, Matron, Necklace, Bowl
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

def index(request):
    #request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        #context={'num_visits': num_visits},
    )


class BeadListView(generic.ListView):
    model = Bead
    
class BeadDetailView(generic.DetailView):
    model = Bead

class BowlListView(generic.ListView):
    model = Bowl
    
class BowlDetailView(generic.DetailView):
    model = Bowl

class NecklaceListView(generic.ListView):
    model = Necklace
    
class NecklaceDetailView(generic.DetailView):
    model = Necklace

class MatronListView(generic.ListView):
    model = Matron
    
class MatronDetailView(generic.DetailView):
    model = Matron
