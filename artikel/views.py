from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Artikel

class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 3

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = 'artikel'
