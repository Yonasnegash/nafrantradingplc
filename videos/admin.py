from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_active',)
    search_fields = ('name', 'sub_title',)
    list_per_page = 25

admin.site.register(Video, VideoAdmin)
