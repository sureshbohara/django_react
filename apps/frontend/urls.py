from django.urls import path
from . import views
app_name = 'frontend'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop/', views.shop_view, name='shop'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
    
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/apply-coupon/', views.apply_coupon, name='apply_coupon'),
    
    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout/place-order/', views.place_order, name='place_order'),
    path('order/success/<int:order_id>/', views.order_success_view, name='order_success'),
    path('my-orders/', views.my_orders_view, name='my_orders'), 
    
    path('customer/login/', views.customer_login, name='customer_login'),
    path('customer/register/', views.customer_register, name='customer_register'),
    path('customer/logout/', views.customer_logout, name='customer_logout'),
]