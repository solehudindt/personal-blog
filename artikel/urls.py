from django.urls import path

from .views import ArtikelListView, ArtikelDetailView

app_name = 'artikel'
urlpatterns = [
    path('<slug>', ArtikelDetailView.as_view(), name='detail'),
    path('', ArtikelListView.as_view(), name='list'),
]
