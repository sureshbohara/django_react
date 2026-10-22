from django.db import models
from django.utils import timezone

class Coupon(models.Model):
    DISCOUNT_TYPES = [('fixed', 'Fixed'), ('percentage', 'Percentage')]
    code = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPES, default='fixed')
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    usage_limit = models.IntegerField(null=True, blank=True)
    used_count = models.IntegerField(default=0)
    usage_limit_per_user = models.IntegerField(default=1)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self): return self.code

    @property
    def is_active(self):
        if not self.status: return False
        now = timezone.now().date()
        if self.start_date and now < self.start_date: return False
        if self.end_date and now > self.end_date: return False
        if self.usage_limit and self.used_count >= self.usage_limit: return False
        return True