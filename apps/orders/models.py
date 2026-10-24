from django.db import models
from customers.models import Customer
from products.models import Product, ProductVariant
import datetime
import random

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery (COD)'),
        ('esewa', 'eSewa'),
        ('khalti', 'Khalti'),
        ('bank', 'Bank Transfer'),
    ]

    order_number = models.CharField(max_length=50, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='orders')
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cod')
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending')
    
    shipping_name = models.CharField(max_length=255)
    shipping_phone = models.CharField(max_length=20)
    shipping_address = models.TextField()
    shipping_city = models.CharField(max_length=100)
    shipping_notes = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order #{self.order_number}"

    def save(self, *args, **kwargs):
        if not self.order_number:
            date_str = datetime.datetime.now().strftime('%Y%m%d')
            
            # FIX 1: Use zfill to ensure it's always 4 digits (e.g., '0005' instead of '5')
            cust_id = str(self.customer.id).zfill(4) if self.customer else '0000'
            
            # FIX 2: Add a random 3-digit suffix to prevent unique constraint errors 
            # if the same customer places multiple orders on the same day.
            random_suffix = random.randint(100, 999)
            self.order_number = f"ORD-{date_str}-{cust_id}{random_suffix}"
            
        self.total_amount = self.subtotal - self.discount + self.shipping_cost
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    
    # FIX 3: Added variant fields since your API cart supports variant_id
    variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True, blank=True)
    variant_name = models.CharField(max_length=255, blank=True, null=True)
    
    product_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        variant_str = f" ({self.variant_name})" if self.variant_name else ""
        return f"{self.quantity}x {self.product_name}{variant_str}"

    @property
    def total(self):
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        # Auto-fill product snapshot if not provided
        if self.product and not self.product_name:
            self.product_name = self.product.name
            self.product_sku = self.product.sku
            if not self.price:  # Only set price if it wasn't explicitly passed
                self.price = self.product.final_price if hasattr(self.product, 'final_price') else self.product.regular_price
                
        # FIX 3: Auto-fill variant name if variant is provided
        if self.variant and not self.variant_name:
            self.variant_name = self.variant.name 
            
        super().save(*args, **kwargs)