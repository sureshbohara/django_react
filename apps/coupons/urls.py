from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('', views.coupon_list, name='coupon_list'),
    path('create/', views.coupon_create, name='coupon_create'),
    path('<int:pk>/update/', views.coupon_update, name='coupon_update'),
    path('<int:pk>/delete/', views.coupon_delete, name='coupon_delete'),
    path('toggle-status/', views.coupon_toggle_status, name='coupon_toggle_status'),
    path('reset-usage/', views.coupon_reset_usage, name='coupon_reset_usage'),
]