from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.page_list, name='page_list'),
    path('create/', views.page_create, name='page_create'),
    path('<int:pk>/update/', views.page_update, name='page_update'),
    path('<int:pk>/delete/', views.page_delete, name='page_delete'),
    path('toggle-status/', views.page_toggle_status, name='page_toggle_status'),
    path('update-order/', views.page_update_order, name='page_update_order'),
]