from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.utils import timezone
from django.http import JsonResponse

from products.models import Product, ProductVariant
from categories.models import Category
from brands.models import Brand
from banners.models import Banner
from reviews.models import Review
from blogs.models import Post
from coupons.models import Coupon

from django.contrib.auth.hashers import check_password, make_password
from customers.models import Customer
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from orders.models import Order, OrderItem 

def home_view(request):
    product_fields = ['id', 'name', 'slug', 'thumbnail', 'regular_price', 'sale_price', 'sale_price_start', 'sale_price_end']
    
    best_sellers = Product.objects.filter(status=True, is_featured=True).only(*product_fields)[:8]
    flash_sale_products = Product.objects.filter(
        status=True, sale_price__isnull=False
    ).exclude(sale_price__gte=F('regular_price')).only(*product_fields)[:4] 
    new_arrivals = Product.objects.filter(status=True).order_by('-created_at').only(*product_fields)[:8]
    
    categories = Category.objects.filter(parent__isnull=True, status=True).prefetch_related('children')[:10]
    banners = Banner.objects.filter(status=True)[:3]
    brands = Brand.objects.filter(status=True)[:12]
    reviews = Review.objects.filter(status=True).order_by('-created_at')[:3]
    blogs = Post.objects.filter(status=True).select_related('category').only(
        'title', 'slug', 'image', 'created_at', 'description', 'category__name'
    )[:3]

    context = {
        'best_sellers': best_sellers,
        'flash_sale_products': flash_sale_products,
        'new_arrivals': new_arrivals,
        'categories': categories,
        'banners': banners,
        'brands': brands,
        'reviews': reviews,
        'blogs': blogs,
    }
    return render(request, 'pages/home.html', context)


def shop_view(request):
    products = Product.objects.filter(status=True).select_related('brand', 'category')
    
    category_slug = request.GET.get('category')
    current_category = None
    if category_slug:
        current_category = Category.objects.filter(slug=category_slug, status=True).first()
        if current_category:
            descendant_categories = current_category.get_all_descendants()
            category_ids = [current_category.id] + [cat.id for cat in descendant_categories]
            products = products.filter(category__id__in=category_ids)
        
    brand_slug = request.GET.get('brand')
    if brand_slug:
        products = products.filter(brand__slug=brand_slug)
        
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        products = products.filter(regular_price__gte=min_price, regular_price__lte=max_price)
    elif min_price:
        products = products.filter(regular_price__gte=min_price)
    elif max_price:
        products = products.filter(regular_price__lte=max_price)

    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(sku__icontains=search_query))

    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'price_low':
        products = products.order_by('regular_price')
    elif sort_by == 'price_high':
        products = products.order_by('-regular_price')
    elif sort_by == 'name':
        products = products.order_by('name')
    else:
        products = products.order_by('-created_at')

    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'products': page_obj,      
        'category': current_category, 
        'categories': Category.objects.filter(parent__isnull=True, status=True).prefetch_related('children'),    
        'brands': Brand.objects.filter(status=True),             
        'filters': request.GET,      
    }
    return render(request, 'pages/shop.html', context)


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, status=True)
    Product.objects.filter(id=product.id).update(view_count=F('view_count') + 1)
    product.refresh_from_db() 
    
    related_products = Product.objects.filter(
        category=product.category, status=True
    ).exclude(id=product.id).only(
        'id', 'name', 'slug', 'thumbnail', 'regular_price', 'sale_price', 'sale_price_start', 'sale_price_end'
    )[:4]
    
    return render(request, 'pages/product_detail.html', {
        'product': product,
        'related_products': related_products,
    })


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        qty = int(request.POST.get('qty', 1))
        variant_id = request.POST.get('variant_id')  
        
     
        if not variant_id or str(variant_id).lower() in ['none', 'undefined', '']:
            variant_id = None
            
        cart_key = f"{product_id}_{variant_id}" if variant_id else str(product_id)
        cart = request.session.get('cart', {})
        
        if cart_key in cart:
            cart[cart_key]['qty'] += qty
        else:
            cart[cart_key] = {'qty': qty, 'variant_id': variant_id}
            
        request.session['cart'] = cart
        request.session.modified = True
        
        total_items = sum(item['qty'] for item in cart.values())
        return JsonResponse({'success': True, 'cart_count': total_items, 'message': 'Added to cart!'})
    return JsonResponse({'success': False}, status=400)


def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0
    
    valid_cart = {}
    for cart_key, item_data in cart.items():
        if isinstance(item_data, dict) and 'qty' in item_data:
            valid_cart[cart_key] = item_data
            
    if len(valid_cart) != len(cart):
        request.session['cart'] = valid_cart
        request.session.modified = True

    for cart_key, item_data in valid_cart.items():
        parts = cart_key.split('_')
        product_id = parts[0]
        variant_id = parts[1] if len(parts) > 1 else None
        
        try:
            product = Product.objects.get(id=int(product_id), status=True)
            
            item_price = product.final_price
            variant_name = "Standard"
            
            # Check if variant_id is a valid numeric string
            if variant_id and str(variant_id).isdigit():
                try:
                    variant = ProductVariant.objects.get(
                        id=int(variant_id), 
                        product=product,
                        status=True
                    )
                    item_price = variant.sale_price if variant.sale_price else variant.price
                    
                    if variant.attributes:
                        variant_parts = []
                        for key, value in variant.attributes.items():
                            variant_parts.append(f"{key}: {value}")
                        variant_name = ", ".join(variant_parts)
                    else:
                        variant_name = "Variant"
                except ProductVariant.DoesNotExist:
                    # Silently fallback to standard if variant was deleted or inactive
                    variant_name = "Standard"
            else:
                variant_name = "Standard"

            item_total = item_price * item_data['qty']
            subtotal += item_total
            
            cart_items.append({
                'product': product,
                'variant_name': variant_name,
                'item_price': item_price,
                'qty': item_data['qty'],
                'item_total': item_total,
                'cart_key': cart_key 
            })
        except (Product.DoesNotExist, ValueError):
            continue
            
    # Coupon Logic
    discount = 0
    coupon_code = request.session.get('coupon_code', '')
    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code, status=True)
            if coupon.discount_type == 'percentage':
                discount = subtotal * (coupon.discount_value / 100)
            else:
                discount = coupon.discount_value
        except Exception:
            pass

    total = subtotal - discount

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'discount': discount,
        'total': total,
        'coupon_code': coupon_code
    }
    return render(request, 'pages/cart.html', context)


def update_cart(request):
    if request.method == 'POST':
        cart_key = request.POST.get('cart_key')
        qty = int(request.POST.get('qty'))
        cart = request.session.get('cart', {})
        
        if cart_key in cart:
            if qty > 0:
                cart[cart_key]['qty'] = qty
            else:
                del cart[cart_key]
            request.session['cart'] = cart
            request.session.modified = True
            
        total_items = sum(item['qty'] for item in cart.values())
        return JsonResponse({'success': True, 'cart_count': total_items})
    return JsonResponse({'success': False}, status=400)


def remove_from_cart(request):
    if request.method == 'POST':
        cart_key = request.POST.get('cart_key')
        cart = request.session.get('cart', {})
        
        if cart_key in cart:
            del cart[cart_key]
            request.session['cart'] = cart
            request.session.modified = True
            
        total_items = sum(item['qty'] for item in cart.values())
        return JsonResponse({'success': True, 'cart_count': total_items})
    return JsonResponse({'success': False}, status=400)


def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('code', '').strip().upper()
        cart = request.session.get('cart', {})
        subtotal = 0
        
        for cart_key, item_data in cart.items():
            if not isinstance(item_data, dict) or 'qty' not in item_data:
                continue
                
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
                        
                subtotal += item_price * item_data['qty']
            except (Product.DoesNotExist, ValueError):
                continue

        try:
            coupon = Coupon.objects.get(code=code, status=True)
            discount = subtotal * (coupon.discount_value / 100) if coupon.discount_type == 'percentage' else coupon.discount_value
                
            request.session['coupon_code'] = code
            request.session.modified = True
            
            return JsonResponse({
                'success': True, 
                'discount': round(discount, 2),
                'total': round(subtotal - discount, 2),
                'message': 'Coupon applied successfully!'
            })
        except Coupon.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid or expired coupon code.'}, status=400)
    return JsonResponse({'success': False}, status=400)









def customer_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email, is_active=True)
            if customer.password and check_password(password, customer.password):
                request.session['customer_id'] = customer.id
                return JsonResponse({'success': True, 'message': 'Login successful!'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid email or password.'}, status=401)
        except Customer.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Customer not found.'}, status=401)
            
    return JsonResponse({'success': False}, status=400)



def customer_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if Customer.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'This email is already registered.'}, status=400)   
        
        try:
            customer = Customer.objects.create(
                name=name,
                email=email,
                password=password 
            )
            request.session['customer_id'] = customer.id
    
            return JsonResponse({'success': True, 'message': 'Account created successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Registration failed: {str(e)}'}, status=400)
            
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)


# 3. Customer Logout
def customer_logout(request):
    if 'customer_id' in request.session:
        del request.session['customer_id']
    return redirect('frontend:home')


@login_required 
def checkout_view(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('frontend:cart')
    customer = get_object_or_404(Customer, id=customer_id, is_active=True)
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0
    
    for cart_key, item_data in cart.items():
        if not isinstance(item_data, dict) or 'qty' not in item_data:
            continue
            
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
            
            item_total = item_price * item_data['qty']
            subtotal += item_total
            
            cart_items.append({
                'product': product,
                'qty': item_data['qty'],
                'item_total': item_total
            })
        except (Product.DoesNotExist, ValueError):
            continue

    total = subtotal 

    context = {
        'customer': customer,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total
    }
    return render(request, 'pages/checkout.html', context)




def place_order(request):
    if request.method == 'POST':

        customer_id = request.session.get('customer_id')
        if not customer_id:
            return redirect('frontend:cart')
            
        customer = get_object_or_404(Customer, id=customer_id, is_active=True)
 
     
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('frontend:cart')
        
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        notes = request.POST.get('order_notes', '')
        payment_method = request.POST.get('payment_method', 'cod')
        

        subtotal = 0
        shipping_cost = 0  
        discount = 0
        

        if 'coupon_code' in request.session:
            del request.session['coupon_code']

        for cart_key, item_data in cart.items():
            if not isinstance(item_data, dict) or 'qty' not in item_data:
                continue
                
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
                
                subtotal += item_price * item_data['qty']
            except (Product.DoesNotExist, ValueError):
                continue
                
        total_amount = subtotal - discount + shipping_cost
        
        # Order Create
        order = Order.objects.create(
            customer=customer,
            subtotal=subtotal,
            discount=discount,
            shipping_cost=shipping_cost,
            total_amount=total_amount,
            payment_method=payment_method,
            shipping_name=full_name,
            shipping_phone=phone,
            shipping_address=address,
            shipping_city=city,
            shipping_notes=notes,
            status='pending',
            payment_status='pending'
        )
        

        for cart_key, item_data in cart.items():
            if not isinstance(item_data, dict) or 'qty' not in item_data:
                continue
                
            parts = cart_key.split('_')
            product_id = parts[0]
            variant_id = parts[1] if len(parts) > 1 else None
            
            try:
                product = Product.objects.get(id=int(product_id), status=True)
                item_price = product.final_price
                product_name = product.name
                product_sku = product.sku
                
          
                if variant_id and str(variant_id).isdigit():
                    try:
                        variant = ProductVariant.objects.get(id=int(variant_id), product=product, status=True)
                        item_price = variant.sale_price if variant.sale_price else variant.price
                        if variant.attributes:
                            variant_info = ", ".join([f"{k}: {v}" for k, v in variant.attributes.items()])
                            product_name = f"{product.name} ({variant_info})"
                    except ProductVariant.DoesNotExist:
                        pass
                
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    product_name=product_name,
                    product_sku=product_sku,
                    quantity=item_data['qty'],
                    price=item_price
                )
            except (Product.DoesNotExist, ValueError):
                continue
                
 
        if 'cart' in request.session:
            del request.session['cart']
        if 'coupon_code' in request.session:
            del request.session['coupon_code']
        request.session.modified = True
        
        return redirect('frontend:order_success', order_id=order.id)
        

    return redirect('frontend:checkout')






def order_success_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer__id=request.session.get('customer_id'))
    
    context = {
        'order': order
    }
    return render(request, 'pages/order_success.html', context)



def my_orders_view(request):
    customer_id = request.session.get('customer_id')
    if not customer_id:
        return redirect('frontend:customer_login')
    
    orders = Order.objects.filter(customer_id=customer_id).prefetch_related('items')
    
    context = {
        'orders': orders
    }
    return render(request, 'pages/my_orders.html', context)