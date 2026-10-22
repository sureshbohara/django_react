from django.urls import path
from . import views

app_name = 'galleries'

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('create/', views.gallery_create, name='gallery_create'),
    path('<int:pk>/update/', views.gallery_update, name='gallery_update'),
    path('<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),
    path('toggle-status/', views.gallery_toggle_status, name='gallery_toggle_status'),
    path('update-order/', views.gallery_update_order, name='gallery_update_order'),
]