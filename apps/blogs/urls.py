from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/update/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('toggle-status/', views.post_toggle_status, name='post_toggle_status'),
    path('update-order/', views.post_update_order, name='post_update_order'),
]