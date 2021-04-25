from django.contrib import admin

from .models import Apartment

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'square_meter', 'price', 'is_negotiabale', 'master_bedroom', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_editable = ('is_published', 'is_negotiabale')
    search_fields = ('title', 'square_meter', 'master_bedroom', 'is_published')
    list_per_page = 25

admin.site.register(Apartment, ApartmentAdmin)
