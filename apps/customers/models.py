from django.db import models
from django.contrib.auth.hashers import make_password 

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True, help_text="Additional info or notes about the customer")
    image = models.ImageField(upload_to='customers/', blank=True, null=True)
    

    password = models.CharField(max_length=128, blank=True, null=True, help_text="Hashed password for frontend login")
    
    is_active = models.BooleanField(default=True)
    subscribed_to_newsletter = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f"{self.name} ({self.email})"

    def save(self, *args, **kwargs):

        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/default/noimage.png'