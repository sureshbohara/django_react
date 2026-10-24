from rest_framework import serializers

from products.models import Product, ProductVariant, ProductAttribute
from categories.models import Category
from brands.models import Brand
from banners.models import Banner
from reviews.models import Review
from blogs.models import Post
from customers.models import Customer
from orders.models import Order, OrderItem
from coupons.models import Coupon
from pages.models import Page
from faqs.models import Faq
from site_settings.models import SiteSetting


# ==========================================
# 1. SITE SETTINGS SERIALIZER
# ==========================================
class SiteSettingSerializer(serializers.ModelSerializer):
    logo_url = serializers.CharField(read_only=True)
    favicon_url = serializers.CharField(read_only=True)
    bg_image_url = serializers.CharField(read_only=True)
    footer_gateway_img_url = serializers.CharField(read_only=True)
    
    class Meta:
        model = SiteSetting
        fields = [
            'id', 'system_name', 'email', 'phone', 'address',
            'logo_url', 'favicon_url', 'bg_image_url', 'footer_gateway_img_url',
            'meta_title', 'meta_keywords', 'meta_description',
            'facebook', 'twitter', 'instagram', 'youtube'
        ]


# ==========================================
# 2. BANNER SERIALIZER
# ==========================================
class BannerSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(read_only=True)
    
    class Meta:
        model = Banner
        fields = ['id', 'title', 'subtitle', 'image_url', 'description', 'order_level']


# ==========================================
# 3. CATEGORY SERIALIZER (Recursive Children)
# ==========================================
class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(read_only=True)
    children = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image_url', 'font_icon', 'children']
    
    def get_children(self, obj):
        children = obj.children.filter(status=True)
        return CategorySerializer(children, many=True).data


# ==========================================
# 4. BRAND SERIALIZER
# ==========================================
class BrandSerializer(serializers.ModelSerializer):
    logo_url = serializers.CharField(read_only=True)
    
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'logo_url', 'website']


# ==========================================
# 5. PRODUCT VARIANT SERIALIZER
# ==========================================
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'sku', 'price', 'sale_price', 'stock_quantity', 'attributes', 'image', 'status']


# ==========================================
# 6. PRODUCT LIST SERIALIZER 
# ==========================================
class ProductListSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.CharField(read_only=True)
    final_price = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    is_on_sale = serializers.BooleanField(read_only=True)
    
    category_name = serializers.CharField(source='category.name', read_only=True, allow_null=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True, allow_null=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'thumbnail_url', 'sku',
            'regular_price', 'sale_price', 'final_price', 'is_on_sale',
            'stock_quantity', 'stock_status', 'category_name', 'brand_name',
            'is_featured', 'view_count'
        ]


# ==========================================
# 7. PRODUCT DETAIL SERIALIZER 
# ==========================================
class ProductDetailSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.CharField(read_only=True)
    final_price = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    is_on_sale = serializers.BooleanField(read_only=True)
    
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    
    # FIX: Used SerializerMethodField to safely filter variants
    variants = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'sku', 'barcode', 'product_type',
            'regular_price', 'sale_price', 'sale_price_start', 'sale_price_end',
            'final_price', 'is_on_sale',
            'manage_stock', 'stock_quantity', 'stock_status',
            'short_description', 'description', 'tags',
            'thumbnail_url', 'gallery', 'video_url', 'faqs',
            'category', 'brand', 'variants',
            'is_featured', 'is_virtual', 'view_count',
            'meta_title', 'meta_keywords', 'meta_description',
            'created_at', 'updated_at'
        ]

    def get_variants(self, obj):
        """Fetch only active variants for the product"""
        active_variants = obj.variants.filter(status=True)
        return ProductVariantSerializer(active_variants, many=True).data


# ==========================================
# 8. REVIEW SERIALIZER
# ==========================================
class ReviewSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(read_only=True)
    star_rating = serializers.CharField(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'name', 'rating', 'review', 'image_url', 'star_rating', 'created_at']


# ==========================================
# 9. BLOG SERIALIZER
# ==========================================
class BlogListSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True, allow_null=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'image_url', 'excerpt', 
            'category_name', 'views', 'is_featured', 'created_at'
        ]

class BlogDetailSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'image_url', 'excerpt', 'description',
            'category', 'views', 'is_featured', 
            'meta_title', 'meta_keywords', 'meta_description',
            'created_at', 'updated_at'
        ]


# ==========================================
# 10. CUSTOMER SERIALIZERS
# ==========================================
class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'password']
    
    def create(self, validated_data):
        """Password automatically hash हुन्छ (model.save() मा)"""
        return Customer.objects.create(**validated_data)

class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class CustomerProfileSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'address', 'image_url']


# ==========================================
# 11. ORDER SERIALIZERS
# ==========================================
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(read_only=True)
    variant_name = serializers.CharField(read_only=True) # Added variant name
    product_thumbnail = serializers.SerializerMethodField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'variant', 'product_name', 'variant_name', 'product_thumbnail', 'quantity', 'price', 'total']
    
    def get_product_thumbnail(self, obj):
        if obj.product and obj.product.thumbnail:
            return obj.product.thumbnail.url
        return None

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_items = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'status', 'payment_status',
            'subtotal', 'discount', 'shipping_cost', 'total_amount',
            'payment_method', 'created_at', 'items', 'total_items'
        ]
    
    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())


# ==========================================
# 12. COUPON SERIALIZER
# ==========================================
class CouponSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'discount_type', 'discount_value', 'is_active']


# ==========================================
# 13. PAGE & FAQ SERIALIZERS
# ==========================================
class PageSerializer(serializers.ModelSerializer):
    image_url = serializers.CharField(read_only=True)
    
    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'content', 'image_url', 'short_content']

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer', 'order_level']