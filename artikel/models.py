from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Artikel(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    judul = models.CharField(max_length=75)
    gambar = models.ImageField(upload_to="images")
    isi = models.TextField()
    kategori = models.CharField(max_length=15)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    # def get_absolute_url(self):
    #     url_slug = {'slug':self.slug}
    #     return reverse('artikel:detail', kwargs = url_slug)   

    def __str__(self):
        return "{} - {}".format(self.id, self.judul)
    