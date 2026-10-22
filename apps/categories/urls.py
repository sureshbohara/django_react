from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('create/', views.category_create, name='category_create'),
    path('<int:pk>/update/', views.category_update, name='category_update'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('toggle-status/', views.category_toggle_status, name='category_toggle_status'),
    path('update-order/', views.category_update_order, name='category_update_order'),
]