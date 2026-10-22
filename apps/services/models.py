from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., bi bi-plane")
    short_content = models.TextField(blank=True, null=True)
    long_content = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    feature_image = models.ImageField(upload_to='services/features/', blank=True, null=True)
    
    process_title = models.CharField(max_length=255, blank=True, null=True)
    process_sub_title = models.CharField(max_length=255, blank=True, null=True)
    process_item = models.JSONField(blank=True, null=True, default=list)
    
    highlight = models.JSONField(blank=True, null=True, default=dict)
    
    order_level = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order_level', '-created_at']
        indexes = [
            models.Index(fields=['order_level']),
            models.Index(fields=['status']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        return self.image.url if self.image and hasattr(self.image, 'url') else '/static/default/noimage.png'

    @property
    def feature_image_url(self):
        return self.feature_image.url if self.feature_image and hasattr(self.feature_image, 'url') else '/static/default/noimage.png'