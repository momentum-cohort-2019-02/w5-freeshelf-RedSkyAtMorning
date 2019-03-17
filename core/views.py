from django.shortcuts import render, get_object_or_404, redirect
from core.models import Bead, Matron, Necklace, Bowl, Dressing, Outfitting, Beat, Drumming, Shoe, Dress
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
#from django.contrib.auth.decorators import login_required
#from django.views.decorators.http import require_http_methods
from core.forms import AddOrShowBead


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

class DressingListView(generic.ListView):
    model = Dressing
    
class DressingDetailView(generic.DetailView):
    model = Dressing

class OutfittingListView(generic.ListView):
    model = Outfitting
    
class OutfittingDetailView(generic.DetailView):
    model = Outfitting

class BeatListView(generic.ListView):
    model = Beat
    
class BeatDetailView(generic.DetailView):
    model = Beat

class DrummingListView(generic.ListView):
    model = Drumming
    
class DrummingDetailView(generic.DetailView):
    model = Drumming

class ShoeListView(generic.ListView):
    model = Shoe
    
class ShoeDetailView(generic.DetailView):
    model = Shoe

class DressListView(generic.ListView):
    model = Dress
    
class DressDetailView(generic.DetailView):
    model = Dress





##Forms Section ##
from core.forms import AddOrShowBead

def add_model(request):
 
    if request.method == "POST":
        form = AddOrShowBead(request.POST)
        if form.is_valid():
            bead_instance = form.save(commit=False)
            bead_instance.save()
            return redirect('/')
 
    else:
 
        form = AddOrShowBead()

    return render(request, "bead_list.html", {'form': form})


# class AddOrShowBeadView(FormView):
#     model = Bead
#     template_name = "bead_list.html"
#     form_class = AddOrShowBead
#     success_url = "/core/beads/"

#     def form_valid(self)
#         return super().form_valid(form)

class DressingCreate(CreateView):
    model = Dressing
    fields = ('dress_id', 'matron_id', 'pk')

class OutfittingCreate(CreateView):
    model = Outfitting
    fields = ('dress_id', 'shoe_id', 'matron_id',)

class BeatCreate(CreateView):
    model = Beat
    fields = ('__all__')

class DrummingCreate(CreateView):
    model = Drumming
    fields = ('beat_id', 'matron_id')

class ShoeCreate(CreateView):
    model = Shoe
    fields = ('__all__')

class DressCreate(CreateView):
    model = Dress
    fields = ('__all__')

class BeadCreate(CreateView):
    model = Bead
    fields = ('__all__')

class MatronCreate(CreateView):
    model = Matron
    fields = ('name', 'linkedin', 'description',)