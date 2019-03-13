## This is catalog.urls

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

# from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'), ),
    path('beads/', TemplateView.as_view(template_name='core/bead-list.html'), ),
    path('beads/<int:pk>', TemplateView.as_view(template_name='core/bead-detail.html'), ),
    path('matrons/', TemplateView.as_view(template_name='core/matron-list.html'), ),
    path('matrons/<int:pk>', TemplateView.as_view(template_name='core/matron-detail.html'), ),
    path('necklaces/', TemplateView.as_view(template_name='core/necklace-list.html'), ),
    path('necklaces/<int:pk>/', TemplateView.as_view(template_name='core/necklaces-detail.html'), ),
    path('bowls/', TemplateView.as_view(template_name='core/bowl-list.html'), ),
    path('bowls/<int:pk>/', TemplateView.as_view(template_name='core/bowl-detail,html'), ),
]

#urlpatterns = [
   # path('', TemplateView.as_view(), name = 'index'),
   # path('beads/', TemplateView.as_view(), name='beads-list'),
   # path('beads/<int:pk>', TemplateView.as_view(), name='beads-detail'),
   # path('matrons/', TemplateView.as_view(), name='matrons-list'),
   # path('matrons/<int:pk>', TemplateView.as_view(), name='matrons-detail'),
   # path('necklaces/', TemplateView.as_view(), name='necklaces-list'),
   # path('necklaces/<int:pk>/', TemplateView.as_view(), name='necklaces-detail'),
   # path('bowls/', TemplateView.as_view(), name='bowls-list'),
   # path('bowls/<int:pk>/', TemplateView.as_view(), name='bowls-detail'),
#]