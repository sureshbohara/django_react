from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Product(models.Model):
    PRODUCT_TYPES = [('simple', 'Simple'), ('variable', 'Variable'), ('grouped', 'Grouped'), ('digital', 'Digital')]
    STOCK_STATUS = [('in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock'), ('on_backorder', 'On Backorder')]

    brand = models.ForeignKey('brands.Brand', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True)
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    sku = models.CharField(max_length=100, unique=True, null=True, blank=True)
    barcode = models.CharField(max_length=100, null=True, blank=True)
    
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES, default='simple')
    
    regular_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sale_price_start = models.DateField(null=True, blank=True)
    sale_price_end = models.DateField(null=True, blank=True)
    
    manage_stock = models.BooleanField(default=True)
    stock_quantity = models.IntegerField(default=0)
    stock_status = models.CharField(max_length=20, choices=STOCK_STATUS, default='in_stock')
    low_stock_threshold = models.IntegerField(default=5)
    
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.JSONField(null=True, blank=True, default=list)
    
    thumbnail = models.ImageField(upload_to='products/', null=True, blank=True)
    gallery = models.JSONField(null=True, blank=True, default=list)
    video_url = models.URLField(null=True, blank=True)
    faqs = models.JSONField(null=True, blank=True, default=list)
    
    downloadable_file = models.FileField(upload_to='products/downloads/', null=True, blank=True)
    download_limit = models.IntegerField(null=True, blank=True)
    download_expiry_days = models.IntegerField(null=True, blank=True)
    
    is_featured = models.BooleanField(default=False)
    is_virtual = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    order_level = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    meta_description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order_level', '-created_at']

    def __str__(self): return self.name

    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def thumbnail_url(self):
        return self.thumbnail.url if self.thumbnail and hasattr(self.thumbnail, 'url') else '/static/default/noimage.png'

    @property
    def final_price(self):
        if self.sale_price and self.sale_price < (self.regular_price or 0):
            now = timezone.now().date()
            if self.sale_price_start and now < self.sale_price_start: return self.regular_price
            if self.sale_price_end and now > self.sale_price_end: return self.regular_price
            return self.sale_price
        return self.regular_price

    @property
    def is_on_sale(self):
        return bool(self.final_price and self.final_price < (self.regular_price or 0))


class ProductAttribute(models.Model):
    TYPE_CHOICES = [('select', 'Select'), ('text', 'Text'), ('color', 'Color'), ('image', 'Image')]
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='select')
    values = models.JSONField(null=True, blank=True, default=list)
    order_level = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return self.name
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    sku = models.CharField(max_length=100, unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    stock_quantity = models.IntegerField(default=0)
    attributes = models.JSONField(null=True, blank=True, default=dict)
    image = models.ImageField(upload_to='products/variants/', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return f"Variant of {self.product.name} ({self.sku})"


class ProductBundle(models.Model):
    parent_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bundle_items')
    child_product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='bundled_in')
    quantity = models.IntegerField(default=1)
    sort_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('parent_product', 'child_product')