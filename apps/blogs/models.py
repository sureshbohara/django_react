from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    excerpt = models.TextField(null=True, blank=True, help_text="Brief excerpt/summary")
    description = models.TextField(help_text="Main blog content")
    
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    
    views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    order_level = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order_level', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/default/noimage.png'