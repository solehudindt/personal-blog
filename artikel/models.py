from django.db import models
from django.utils.text import slugify

class Artikel(models.Model):
    judul = models.CharField(max_length=75)
    gambar = models.ImageField(upload_to="images")
    isi = models.TextField()
    kategori = models.CharField(max_length=15)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def __str__(self):
        return "{} - {}".format(self.id, self.judul)
    