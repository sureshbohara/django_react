from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Sum
from django.utils import timezone

from products.models import Product
from categories.models import Category
from reviews.models import Review
from orders.models import Order
from customers.models import Customer

@login_required
def dashboard_view(request):
    # 1. Basic Counts
    total_products = Product.objects.count()
    active_products = Product.objects.filter(status=True).count()
    
    total_categories = Category.objects.count()
    total_reviews = Review.objects.count()
    
    # 2. E-commerce Stats (Orders & Customers)
    total_orders = Order.objects.count()
    
    # Total Revenue (Delivered, Shipped, & Processing)
    revenue_data = Order.objects.filter(status__in=['delivered', 'shipped', 'processing']).aggregate(Sum('total_amount'))
    total_revenue = revenue_data['total_amount__sum'] or 0
    
    total_customers = Customer.objects.count()
    
    # New Customers This Month
    now = timezone.now()
    new_customers = Customer.objects.filter(created_at__month=now.month, created_at__year=now.year).count()

    # Pending Orders (Action Required)
    pending_orders = Order.objects.filter(status='pending').count()
    
    # 3. Chart Data: Last 7 Days Orders
    today = datetime.now().date()
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    chart_labels = [day.strftime('%a') for day in last_7_days] 
    
    chart_data = []
    for day in last_7_days:
        count = Order.objects.filter(created_at__date=day).count()
        chart_data.append(count)

    # 4. Recent Orders (Latest 5)
    recent_orders = Order.objects.select_related('customer').order_by('-created_at')[:5]

    context = {
        'total_products': total_products,
        'active_products': active_products,
        'total_categories': total_categories,
        'total_reviews': total_reviews,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'total_customers': total_customers,
        'new_customers': new_customers,
        'pending_orders': pending_orders,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'recent_orders': recent_orders,
    }
    
    return render(request, "admin/core/dashboard.html", context)