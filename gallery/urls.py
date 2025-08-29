from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('api/media/', views.media_api, name='media_api'),
]