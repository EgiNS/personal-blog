from django.contrib import admin
from myblog.models import Halaman #Harus berurutan
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul']
    search_fields = ['judul']
    list_filter = ['judul']
    list_per_page = 10

admin.site.register(Halaman)