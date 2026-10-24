from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # Site Settings
    path('settings/', views.get_site_settings, name='site_settings'),
    
    # Banners
    path('banners/', views.banner_list, name='banner_list'),
    
    # Categories & Brands
    path('categories/', views.category_list, name='category_list'),
    path('brands/', views.brand_list, name='brand_list'),
    
    # Products
    path('products/latest/', views.get_latest_product_data, name='latest_products'),
    path('products/featured/', views.get_featured_product_data, name='featured_products'),
    path('products/flash-sale/', views.get_flash_sale_data, name='flash_sale'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Reviews & Blogs
    path('reviews/', views.review_list, name='review_list'),
    path('blogs/', views.blog_list, name='blog_list'),
    
    # Pages & FAQs
    path('pages/', views.page_list, name='page_list'),
    path('faqs/', views.faq_list, name='faq_list'),
    
    # Customer Auth
    path('auth/register/', views.customer_register, name='register'),
    path('auth/login/', views.customer_login, name='login'),
    path('auth/profile/', views.customer_profile, name='profile'),
    
    # Cart
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    
    # Coupons
    path('coupons/apply/', views.apply_coupon, name='apply_coupon'),
    
    # Orders
    path('orders/', views.customer_orders, name='customer_orders'),
    path('orders/create/', views.create_order, name='create_order'),
]