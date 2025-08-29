from django.contrib import admin
from .models import MediaItem


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type', 'is_featured', 'order', 'uploaded_at']
    list_filter = ['media_type', 'is_featured', 'uploaded_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured', 'order']
    ordering = ['order', '-uploaded_at']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'file')
        }),
        ('Configurações', {
            'fields': ('thumbnail', 'is_featured', 'order')
        }),
    )
    
    readonly_fields = ['media_type']
