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
    path('beads/<int:pk>/', views.BeadDetailView.as_view(), name='bead_detail'),
    path('matrons/', views.MatronListView.as_view(), name='matron_list'),
    path('matrons/<int:pk>', views.MatronDetailView.as_view(), name='matron_detail'),
    path('necklaces/', views.NecklaceListView.as_view(), name='necklace_list'),
    path('necklaces/<int:pk>/', views.NecklaceDetailView.as_view(), name='necklace_detail'),
    path('bowls/', views.BowlListView.as_view(), name='bowl_list'),
    path('bowls/<int:pk>/', views.BowlDetailView.as_view(), name='bowl_detail'),
]