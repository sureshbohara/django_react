from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Products
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('toggle-status/', views.product_toggle_status, name='product_toggle_status'),
    path('update-order/', views.product_update_order, name='product_update_order'),
    
    # Attributes
    path('attributes/', views.attribute_list, name='attribute_list'),
    path('attributes/create/', views.attribute_create, name='attribute_create'),
    path('attributes/<int:pk>/update/', views.attribute_update, name='attribute_update'),
    path('attributes/<int:pk>/delete/', views.attribute_delete, name='attribute_delete'),
    path('attributes/toggle-status/', views.attribute_toggle_status, name='attribute_toggle_status'),
    path('attributes/update-order/', views.attribute_update_order, name='attribute_update_order'),
    
    # Variants
    path('<int:product_id>/variants/', views.variant_list, name='variant_list'),
    path('<int:product_id>/variants/create/', views.variant_create, name='variant_create'),
    path('variants/<int:pk>/delete/', views.variant_delete, name='variant_delete'),
]