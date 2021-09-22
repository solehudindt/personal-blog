from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Artikel

class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/artikel_list.html"
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 3

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

    def get_queryset(self):
        artikel_kategori = self.model.objects.filter(kategori=self.kwargs['kategori'])
        print(artikel_kategori)

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/artikel_detail.html"
    context_object_name = 'artikel'
