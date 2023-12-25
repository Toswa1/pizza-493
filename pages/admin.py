from django.contrib import admin
from pages.models import ScrollModel, GalleryModel

@admin.register(ScrollModel)
class ScrollModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','dicount', 'created_at']
    search_fields = ['title','description']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at']


@admin.register(GalleryModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ['id','created_at']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at']
