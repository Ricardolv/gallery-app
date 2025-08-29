from django.shortcuts import render
from django.http import JsonResponse
from .models import MediaItem


def gallery_view(request):
    """View principal da galeria com carrossel"""
    media_items = MediaItem.objects.all().order_by('order', '-uploaded_at')
    
    context = {
        'media_items': media_items,
        'total_items': media_items.count(),
    }
    
    return render(request, 'gallery/gallery.html', context)


def media_api(request):
    """API para retornar dados dos itens de mídia em JSON"""
    media_items = MediaItem.objects.all().order_by('order', '-uploaded_at')
    
    data = []
    for item in media_items:
        data.append({
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'media_type': item.media_type,
            'file_url': item.file.url if item.file else '',
            'thumbnail_url': item.thumbnail.url if item.thumbnail else '',
            'is_featured': item.is_featured,
        })
    
    return JsonResponse({'media_items': data})


def home_view(request):
    """View da página inicial"""
    featured_items = MediaItem.objects.filter(is_featured=True).order_by('order', '-uploaded_at')[:6]
    recent_items = MediaItem.objects.all().order_by('-uploaded_at')[:12]
    
    context = {
        'featured_items': featured_items,
        'recent_items': recent_items,
    }
    
    return render(request, 'gallery/home.html', context)
