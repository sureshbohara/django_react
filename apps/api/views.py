from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.db.models import Q, F, Count
from django.db import transaction  
from django.contrib.auth.hashers import check_password
from django.conf import settings
import jwt
from datetime import datetime, timedelta

from products.models import Product, ProductVariant
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

from .serializers import (
    SiteSettingSerializer, BannerSerializer, CategorySerializer, BrandSerializer,
    ProductListSerializer, ProductDetailSerializer, ReviewSerializer, 
    BlogListSerializer, BlogDetailSerializer,
    CustomerRegisterSerializer, CustomerLoginSerializer, CustomerProfileSerializer,
    OrderSerializer, CouponSerializer, PageSerializer, FaqSerializer
)


# ==========================================
# HELPER: CUSTOM JWT TOKEN
# ==========================================
def get_tokens_for_customer(customer):
    payload = {
        'customer_id': customer.id,
        'exp': datetime.utcnow() + timedelta(days=7),
        'iat': datetime.utcnow(),
        'type': 'customer'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


# ==========================================
# HELPER: PAGINATION
# ==========================================
def paginate_response(request, queryset, serializer_class, page_size=20):
    paginator = Paginator(queryset, page_size)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return {
        'data': serializer_class(page_obj, many=True).data,
        'current_page': page_obj.number,
        'last_page': paginator.num_pages,
        'total': paginator.count,
    }


# ==========================================
# 1. SITE SETTINGS API
# ==========================================
@api_view(['GET'])
@permission_classes([AllowAny])
def get_site_settings(request):
    site_settings = SiteSetting.get_instance()
    return Response({
        'success': True,
        'data': SiteSettingSerializer(site_settings).data
    })


# ==========================================
# 2. BANNERS API
# ==========================================
@api_view(['GET'])
@permission_classes([AllowAny])
def banner_list(request):
    banners = Banner.objects.filter(status=True).order_by('order_level')
    return Response({
        'success': True,
        'data': BannerSerializer(banners, many=True).data
    })


# ==========================================
# 3. CATEGORIES API
# ==========================================
@api_view(['GET'])
@permission_classes([AllowAny])
def category_list(request):
    categories = Category.objects.filter(
        parent__isnull=True, 
        status=True
    ).prefetch_related('children')
    
    return Response({
        'success': True,
        'data': CategorySerializer(categories, many=True).data
    })


# ==========================================
# 4. BRANDS API
# ==========================================
@api_view(['GET'])
@permission_classes([AllowAny])
def brand_list(request):
    brands = Brand.objects.filter(status=True)
    return Response({
        'success': True,
        'data': BrandSerializer(brands, many=True).data
    })


# ==========================================
# 5. PRODUCTS API (Special Views)
# ==========================================
@api_view(['GET'])
@permission_classes([AllowAny])
def get_flash_sale_data(request):
    """Flash sale products"""
    products = Product.objects.filter(
        status=True, 
        sale_price__isnull=False
    ).exclude(
        sale_price__gte=F('regular_price')
    ).select_related('category', 'brand')[:10]
    
    return Response({
        'success': True,
        'data': ProductListSerializer(products, many=True).data
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def get_latest_product_data(request):
    """Latest products"""
    limit = int(request.GET.get('limit', 20))
    products = Product.objects.filter(status=True).select_related('category', 'brand').order_by('-created_at')
    paginated = paginate_response(request, products, ProductListSerializer, page_size=limit)
    
    return Response({
        'success': True,
        **paginated
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def get_featured_product_data(request):
    """Featured products"""
    limit = int(request.GET.get('limit', 20))
    products = Product.objects.filter(
        status=True, 
        is_featured=True
    ).select_related('category', 'brand').order_by('-created_at')
    paginated = paginate_response(request, products, ProductListSerializer, page_size=limit)
    
    return Response({
        'success': True,
        **paginated
    })


# ==========================================
# 6. PRODUCTS API (List & Detail)
# ==========================================
@api_view(['GET'])
@permission_classes([AllowAny])
def product_list(request):
    products = Product.objects.filter(status=True).select_related('category', 'brand')
    
    search = request.GET.get('search')
    if search:
        products = products.filter(
            Q(name__icontains=search) | 
            Q(description__icontains=search) | 
            Q(sku__icontains=search)
        )
    
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    brand_slug = request.GET.get('brand')
    if brand_slug:
        products = products.filter(brand__slug=brand_slug)
    
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(regular_price__gte=min_price)
    if max_price:
        products = products.filter(regular_price__lte=max_price)
    
    sort = request.GET.get('sort', 'newest')
    if sort == 'price_low':
        products = products.order_by('regular_price')
    elif sort == 'price_high':
        products = products.order_by('-regular_price')
    elif sort == 'name':
        products = products.order_by('name')
    else:
        products = products.order_by('-created_at')
    
    page_size = int(request.GET.get('limit', 20))
    paginated = paginate_response(request, products, ProductListSerializer, page_size)
    
    return Response({
        'success': True,
        **paginated
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def product_detail(request, slug):
    try:
        product = Product.objects.select_related('category', 'brand').get(slug=slug, status=True)
        
        Product.objects.filter(id=product.id).update(view_count=F('view_count') + 1)
        product.refresh_from_db()
        
        return Response({
            'success': True,
            'data': ProductDetailSerializer(product).data
        })
    except Product.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Product not found'
        }, status=status.HTTP_404_NOT_FOUND)


# ==========================================
# 7. REVIEWS & BLOGS API
# ==========================================
@api_view(['GET'])
@permission_classes([AllowAny])
def review_list(request):
    reviews = Review.objects.filter(status=True).order_by('-created_at')[:10]
    return Response({
        'success': True,
        'data': ReviewSerializer(reviews, many=True).data
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def blog_list(request):
    blogs = Post.objects.filter(status=True).select_related('category').order_by('-created_at')[:10]
    return Response({
        'success': True,
        'data': BlogListSerializer(blogs, many=True).data
    })


# ==========================================
# 8. PAGES & FAQS API
# ==========================================
@api_view(['GET'])
@permission_classes([AllowAny])
def page_list(request):
    pages = Page.objects.filter(status=True)
    return Response({
        'success': True,
        'data': PageSerializer(pages, many=True).data
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def faq_list(request):
    faqs = Faq.objects.filter(status=True).order_by('order_level')
    return Response({
        'success': True,
        'data': FaqSerializer(faqs, many=True).data
    })


# ==========================================
# 9. CUSTOMER AUTH APIs
# ==========================================
@api_view(['POST'])
@permission_classes([AllowAny])
def customer_register(request):
    serializer = CustomerRegisterSerializer(data=request.data)
    
    if Customer.objects.filter(email=request.data.get('email')).exists():
        return Response({
            'success': False,
            'message': 'Email already registered'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if serializer.is_valid():
        customer = serializer.save()
        token = get_tokens_for_customer(customer)
        
        return Response({
            'success': True,
            'message': 'Registered successfully',
            'token': token,
            'user': CustomerProfileSerializer(customer).data
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        'success': False,
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def customer_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        customer = Customer.objects.get(email=email, is_active=True)
        
        if customer.password and check_password(password, customer.password):
            token = get_tokens_for_customer(customer)
            
            return Response({
                'success': True,
                'message': 'Login successful',
                'token': token,
                'user': CustomerProfileSerializer(customer).data
            })
        else:
            return Response({
                'success': False,
                'message': 'Invalid email or password'
            }, status=status.HTTP_401_UNAUTHORIZED)
            
    except Customer.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Customer not found'
        }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_profile(request):
    customer = request.user
    return Response({
        'success': True,
        'data': CustomerProfileSerializer(customer).data
    })


# ==========================================
# 10. CART API (Session-based)
# ==========================================
@api_view(['POST'])
@permission_classes([AllowAny])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))
    variant_id = request.data.get('variant_id')
    
    cart = request.session.get('cart', {})
    cart_key = f"{product_id}_{variant_id}" if variant_id else str(product_id)
    
    if cart_key in cart:
        cart[cart_key]['quantity'] += quantity
    else:
        cart[cart_key] = {'quantity': quantity, 'variant_id': variant_id}
    
    request.session['cart'] = cart
    request.session.modified = True
    
    total_items = sum(item['quantity'] for item in cart.values())
    
    return Response({
        'success': True,
        'message': 'Added to cart',
        'cart_count': total_items
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0
    
    for cart_key, item_data in cart.items():
        parts = cart_key.split('_')
        product_id = parts[0]
        variant_id = parts[1] if len(parts) > 1 else None
        
        try:
            product = Product.objects.get(id=int(product_id), status=True)
            item_price = product.final_price
            
            if variant_id and str(variant_id).isdigit():
                try:
                    variant = ProductVariant.objects.get(id=int(variant_id), product=product, status=True)
                    item_price = variant.sale_price if variant.sale_price else variant.price
                except ProductVariant.DoesNotExist:
                    pass
            
            item_total = item_price * item_data['quantity']
            subtotal += item_total
            
            cart_items.append({
                'cart_key': cart_key,
                'product': ProductListSerializer(product).data,
                'quantity': item_data['quantity'],
                'item_price': float(item_price),
                'item_total': float(item_total)
            })
        except (Product.DoesNotExist, ValueError):
            continue
    
    return Response({
        'success': True,
        'items': cart_items,
        'subtotal': float(subtotal)
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def update_cart(request):
    cart_key = request.data.get('cart_key')
    quantity = int(request.data.get('quantity'))
    
    cart = request.session.get('cart', {})
    
    if cart_key in cart:
        if quantity > 0:
            cart[cart_key]['quantity'] = quantity
        else:
            del cart[cart_key]
        
        request.session['cart'] = cart
        request.session.modified = True
        
        total_items = sum(item['quantity'] for item in cart.values())
        
        return Response({
            'success': True,
            'cart_count': total_items
        })
    
    return Response({
        'success': False,
        'message': 'Item not found in cart'
    }, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def remove_from_cart(request):
    cart_key = request.data.get('cart_key')
    
    cart = request.session.get('cart', {})
    
    if cart_key in cart:
        del cart[cart_key]
        request.session['cart'] = cart
        request.session.modified = True
        
        total_items = sum(item['quantity'] for item in cart.values())
        
        return Response({
            'success': True,
            'cart_count': total_items
        })
    
    return Response({
        'success': False,
        'message': 'Item not found in cart'
    }, status=status.HTTP_404_NOT_FOUND)


# ==========================================
# 11. COUPON API
# ==========================================
@api_view(['POST'])
@permission_classes([AllowAny])
def apply_coupon(request):
    code = request.data.get('code', '').strip().upper()
    cart = request.session.get('cart', {})
    subtotal = 0
    
    for cart_key, item_data in cart.items():
        parts = cart_key.split('_')
        product_id = parts[0]
        variant_id = parts[1] if len(parts) > 1 else None
        
        try:
            product = Product.objects.get(id=int(product_id), status=True)
            item_price = product.final_price
            
            if variant_id and str(variant_id).isdigit():
                try:
                    variant = ProductVariant.objects.get(id=int(variant_id), product=product, status=True)
                    item_price = variant.sale_price if variant.sale_price else variant.price
                except ProductVariant.DoesNotExist:
                    pass
            
            subtotal += item_price * item_data['quantity']
        except (Product.DoesNotExist, ValueError):
            continue
    
    try:
        coupon = Coupon.objects.get(code=code, status=True)
        
        if coupon.discount_type == 'percentage':
            discount = subtotal * (coupon.discount_value / 100)
        else:
            discount = coupon.discount_value
        
        request.session['coupon_code'] = code
        request.session.modified = True
        
        return Response({
            'success': True,
            'message': 'Coupon applied successfully',
            'discount': float(discount),
            'total': float(subtotal - discount)
        })
    except Coupon.DoesNotExist:
        return Response({
            'success': False,
            'message': 'Invalid or expired coupon code'
        }, status=status.HTTP_400_BAD_REQUEST)


# ==========================================
# 12. ORDER APIs
# ==========================================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_orders(request):
    customer = request.user
    orders = Order.objects.filter(customer=customer).prefetch_related('items')
    
    return Response({
        'success': True,
        'data': OrderSerializer(orders, many=True).data
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    """नयाँ order create गर्ने"""
    customer = request.user
    cart = request.session.get('cart', {})
    
    if not cart:
        return Response({
            'success': False,
            'message': 'Cart is empty'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    subtotal = 0
    discount = 0
    shipping_cost = 0
    order_items = []
    
    for cart_key, item_data in cart.items():
        parts = cart_key.split('_')
        product_id = parts[0]
        variant_id = parts[1] if len(parts) > 1 else None
        
        try:
            product = Product.objects.get(id=int(product_id), status=True)
            item_price = product.final_price
            
            if variant_id and str(variant_id).isdigit():
                try:
                    variant = ProductVariant.objects.get(id=int(variant_id), product=product, status=True)
                    item_price = variant.sale_price if variant.sale_price else variant.price
                except ProductVariant.DoesNotExist:
                    pass
            
            quantity = item_data['quantity']
            item_total = item_price * quantity
            subtotal += item_total
            
            order_items.append({
                'product': product,
                'product_name': product.name,
                'product_sku': product.sku,
                'quantity': quantity,
                'price': item_price
            })
        except (Product.DoesNotExist, ValueError):
            continue
    
    coupon_code = request.session.get('coupon_code')
    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code, status=True)
            if coupon.discount_type == 'percentage':
                discount = subtotal * (coupon.discount_value / 100)
            else:
                discount = coupon.discount_value
        except Coupon.DoesNotExist:
            pass
    
    total_amount = subtotal - discount + shipping_cost
    
    try:
        with transaction.atomic():
            order = Order.objects.create(
                customer=customer,
                subtotal=subtotal,
                discount=discount,
                shipping_cost=shipping_cost,
                total_amount=total_amount,
                payment_method=request.data.get('payment_method', 'cod'),
                shipping_name=request.data.get('shipping_name', ''),
                shipping_phone=request.data.get('shipping_phone', ''),
                shipping_address=request.data.get('shipping_address', ''),
                shipping_city=request.data.get('shipping_city', ''),
                shipping_notes=request.data.get('shipping_notes', ''),
                status='pending',
                payment_status='pending'
            )
            
            for item_data in order_items:
                OrderItem.objects.create(
                    order=order,
                    product=item_data['product'],
                    product_name=item_data['product_name'],
                    product_sku=item_data['product_sku'],
                    quantity=item_data['quantity'],
                    price=item_data['price']
                )
    except Exception as e:
        return Response({
            'success': False,
            'message': f'Order creation failed: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if 'cart' in request.session:
        del request.session['cart']
    if 'coupon_code' in request.session:
        del request.session['coupon_code']
    request.session.modified = True
    
    return Response({
        'success': True,
        'message': 'Order created successfully',
        'data': OrderSerializer(order).data
    }, status=status.HTTP_201_CREATED)