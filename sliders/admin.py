from django.contrib import admin

from .models import Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'sub_title', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'name', 'sub_title',)
    list_per_page = 25

admin.site.register(Slider, SliderAdmin)
