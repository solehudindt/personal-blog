from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Artikel
from .forms import ArtikelForm
import random

# class ArtikelManageView(ListView):
#     model = Artikel
#     template_name = "artikel/artikel_manage.html"
#     context_object_name = 'artikel'

# class ArtikelCreateView(CreateView):
#     form_class = ArtikelForm
#     template_name = "artikel/artikel_create.html"

class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 3

    def get_queryset(self):
        # Only show published articles
        return self.model.objects.filter(status='published').order_by('-published')

    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)

class ArtikelKategoriView(ListView):
    model = Artikel
    template_name = "artikel/artikel_kategori.html"
    context_object_name = 'artikel_list'
    ordering = ['-published']

    # def get_queryset(self):
    #     self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
    #     return super().get_queryset()
    
    def get_queryset(self):
        # Only show published articles in this category
        self.queryset = self.model.objects.filter(
            kategori=self.kwargs['kategori'],
            status='published'
        )
        return super().get_queryset()

    def get_context_data(self,*args,**kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(
            kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list':kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = 'artikel'

    def get_queryset(self):
        # Only allow viewing published articles
        return self.model.objects.filter(status='published')

    def get_context_data(self,*args,**kwargs):
        related_artk = list(self.model.objects.filter(status='published').exclude(id=self.object.id))
        if len(related_artk) < 3:
            item_count = len(related_artk)
        else:
            item_count = 3
        random_items = random.sample(related_artk, item_count)
        self.kwargs.update({'related_artikel':random_items})

        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)
