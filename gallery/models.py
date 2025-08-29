from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class MediaItem(models.Model):
    MEDIA_TYPES = [
        ('image', 'Imagem'),
        ('video', 'Vídeo'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descrição')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, verbose_name='Tipo de Mídia')
    file = models.FileField(
        upload_to='gallery/%Y/%m/%d/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp4', 'avi', 'mov', 'webm']
            )
        ],
        verbose_name='Arquivo'
    )
    thumbnail = models.ImageField(
        upload_to='gallery/thumbnails/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Miniatura'
    )
    uploaded_at = models.DateTimeField(default=timezone.now, verbose_name='Data de Upload')
    is_featured = models.BooleanField(default=False, verbose_name='Destaque')
    order = models.PositiveIntegerField(default=0, verbose_name='Ordem')
    
    class Meta:
        ordering = ['order', '-uploaded_at']
        verbose_name = 'Item de Mídia'
        verbose_name_plural = 'Itens de Mídia'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Determinar o tipo de mídia baseado na extensão do arquivo
        if self.file:
            file_extension = self.file.name.split('.')[-1].lower()
            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
                self.media_type = 'image'
            elif file_extension in ['mp4', 'avi', 'mov', 'webm']:
                self.media_type = 'video'
        
        super().save(*args, **kwargs)
    
    @property
    def is_image(self):
        return self.media_type == 'image'
    
    @property
    def is_video(self):
        return self.media_type == 'video'
