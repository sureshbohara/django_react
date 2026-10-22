from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    path('', views.brand_list, name='brand_list'),
    path('create/', views.brand_create, name='brand_create'),
    path('<int:pk>/update/', views.brand_update, name='brand_update'),
    path('<int:pk>/delete/', views.brand_delete, name='brand_delete'),
    path('toggle-status/', views.brand_toggle_status, name='brand_toggle_status'),
    path('update-order/', views.brand_update_order, name='brand_update_order'),
]