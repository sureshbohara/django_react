from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    font_icon = models.CharField(max_length=255, null=True, blank=True)
    order_level = models.PositiveIntegerField(default=0)
    display_on = models.CharField(max_length=255, default='default')
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order_level', 'name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/default/noimage.png'

    def get_all_descendants(self):
        """Get all children, grandchildren, etc. recursively"""
        descendants = []
        children = list(self.children.all())
        for child in children:
            descendants.append(child)
            descendants.extend(child.get_all_descendants())
        return descendants