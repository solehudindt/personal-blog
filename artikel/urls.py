from django.urls import path

from .views import ArtikelListView, ArtikelDetailView, ArtikelKategoriView, ArtikelCreateView

app_name = 'artikel'
urlpatterns = [
    path('create', ArtikelCreateView.as_view(), name='create'),
    path('category/<kategori>', ArtikelKategoriView.as_view(), name='category'),
    path('<slug>', ArtikelDetailView.as_view(), name='detail'),
    path('', ArtikelListView.as_view(), name='list'),
]
