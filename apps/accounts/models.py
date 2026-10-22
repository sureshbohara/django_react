from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class AdminUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email: raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('status', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class AdminUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    

    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    
    image = models.ImageField(upload_to='admin_profiles/', null=True, blank=True, default='noimage.png')
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AdminUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self): 
        return self.name

    @property
    def image_url(self):
        if self.image and str(self.image) != 'noimage.png' and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/default/noimage.png'

    def has_perm(self, perm, obj=None): 
        return self.is_active
        
    def has_module_perms(self, app_label): 
        return self.is_active