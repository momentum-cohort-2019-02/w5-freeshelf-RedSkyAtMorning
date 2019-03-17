## This is catalog.urls

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView



from . import views

#urlpatterns = [
 #   path('', TemplateView.as_view(template_name = 'index.html'), ),
#    path('beads/', TemplateView.as_view(template_name='core/bead-list.html'), ),
 #   path('beads/<int:pk>', TemplateView.as_view(template_name='core/bead-detail.html'), ),
 #   path('matrons/', TemplateView.as_view(template_name='core/matron-list.html'), ),
 #   path('matrons/<int:pk>', TemplateView.as_view(template_name='core/matron-detail.html'), ),
 #   path('necklaces/', TemplateView.as_view(template_name='core/necklace-list.html'), ),
 #   path('necklaces/<int:pk>/', TemplateView.as_view(template_name='core/necklaces-detail.html'), ),
 #   path('bowls/', TemplateView.as_view(template_name='core/bowl-list.html'), ),
 #   path('bowls/<int:pk>/', TemplateView.as_view(template_name='core/bowl-detail,html'), ),
#]

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('beads/', views.BeadListView.as_view(), name='bead_list'),
    path('bead/<int:pk>', views.BeadDetailView.as_view(), name='bead_detail'),
    path('matrons/', views.MatronListView.as_view(), name='matron_list'),
    path('matron/<int:pk>', views.MatronDetailView.as_view(), name='matron_detail'),
    path('necklaces/', views.NecklaceListView.as_view(), name='necklace_list'),
    path('necklace/<int:pk>', views.NecklaceDetailView.as_view(), name='necklace_detail'),
    path('bowls/', views.BowlListView.as_view(), name='bowl_list'),
    path('bowl/<int:pk>/', views.BowlDetailView.as_view(), name='bowl_detail'),
    path('bead/add', views.BeadCreate.as_view(), name='bead_create'),
    path('matron/add', views.MatronCreate.as_view(), name='matron_create'),

    path('dressings/', views.DressingListView.as_view(), name='dressing_list'),
    path('dressing/<int:pk>/', views.DressingDetailView.as_view(), name='dressing_detail'),
    path('dressing/add', views.DressingCreate.as_view(), name='dressing_create'),

    path('outfittings/', views.OutfittingListView.as_view(), name='outfitting_list'),
    path('outfitting/<int:pk>/', views.OutfittingDetailView.as_view(), name='outfitting_detail'),
    path('outfitting/add', views.OutfittingCreate.as_view(), name='outfitting_create'),

    path('beats/', views.BeatListView.as_view(), name='beat_list'),
    path('beat/<int:pk>/', views.BeatDetailView.as_view(), name='beat_detail'),
    path('beat/add', views.BeatCreate.as_view(), name='beat_create'),

    path('drummings/', views.DrummingListView.as_view(), name='drumming_list'),
    path('drumming/<int:pk>/', views.DrummingDetailView.as_view(), name='drumming_detail'),
    path('drumming/add', views.DrummingCreate.as_view(), name='drumming_create'),

    path('shoes/', views.ShoeListView.as_view(), name='shoe_list'),
    path('shoe/<int:pk>/', views.ShoeDetailView.as_view(), name='shoe_detail'),
    path('shoe/add', views.ShoeCreate.as_view(), name='shoe_create'),

    path('dresses/', views.DressListView.as_view(), name='dress_list'),
    path('dress/<int:pk>/', views.DressDetailView.as_view(), name='dress_detail'),
    path('dress/add', views.DressCreate.as_view(), name='dress_create'),

]