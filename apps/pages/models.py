from django.db import models
from django.utils.text import slugify

class Page(models.Model):
    title = models.CharField(max_length=255, help_text="e.g., About Our Company")
    menu_title = models.CharField(max_length=255, blank=True, null=True, help_text="Optional: Short name for navigation menu (e.g., About Us)")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    icon = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., bi bi-info-circle")
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    short_content = models.CharField(max_length=500, blank=True, null=True, help_text="Brief summary shown in lists/previews")
    content = models.TextField(blank=True, null=True, help_text="Main page content (Rich Text)")
    
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    
    show_in_menu = models.BooleanField(default=False)
    show_in_footer = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    order_level = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    
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
        return self.image.url if self.image and hasattr(self.image, 'url') else '/static/admin/images/noimage.png'