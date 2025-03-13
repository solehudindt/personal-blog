# admin.py with Summernote integration and draft functionality

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Artikel

class ArtikelAdmin(SummernoteModelAdmin):  # using SummernoteModelAdmin
    summernote_fields = '__all__'
    list_display = ('judul', 'kategori', 'published', 'status')
    list_filter = ('status', 'kategori', 'published')
    search_fields = ('judul', 'isi')
    readonly_fields = [
        'slug',
        'updated',
        'published',
    ]
    actions = ['make_published', 'make_draft']
    
    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='published')
        if rows_updated == 1:
            message_bit = "1 artikel berhasil"
        else:
            message_bit = f"{rows_updated} artikel berhasil"
        self.message_user(request, f"{message_bit} dipublikasikan.")
    make_published.short_description = "Publikasikan artikel yang dipilih"
    
    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status='draft')
        if rows_updated == 1:
            message_bit = "1 artikel berhasil"
        else:
            message_bit = f"{rows_updated} artikel berhasil"
        self.message_user(request, f"{message_bit} dijadikan draft.")
    make_draft.short_description = "Jadikan draft artikel yang dipilih"

admin.site.register(Artikel, ArtikelAdmin)