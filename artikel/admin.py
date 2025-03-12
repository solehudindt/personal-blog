from django.contrib import admin
from .models import Artikel
from django_summernote.admin import SummernoteModelAdmin

# class ArtikelAdmin(admin.ModelAdmin):
#     readonly_fields=[
#         'slug',
#         'updated',
#         'published',
#     ]
# Apply summernote to all TextField in model.
class ArtikelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Artikel, ArtikelAdmin)