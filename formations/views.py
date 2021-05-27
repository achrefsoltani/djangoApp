from django.db.models import Q
from django.shortcuts import render
from django.views.generic import (
    CreateView, 
    ListView, 
    UpdateView, 
    DetailView, 
    DeleteView
)

from .models import Formation

class FormationListView(ListView):


    model = Formation
    template_name = "formations/formation_list.html"
    context_object_name = "formations"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if (query):
            object_list = Formation.objects.filter(
                Q(title__icontains=query) | Q(category__icontains=query)
            )
            return object_list
        else :
            return Formation.objects.filter()
         

class FormationDetailView(DetailView):
    model = Formation
    template_name = "formations/formation_detail.html"
    context_object_name = "formation"