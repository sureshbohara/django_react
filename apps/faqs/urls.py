from django.urls import path
from . import views

app_name = 'faqs'

urlpatterns = [
    path('', views.faq_list, name='faq_list'),
    path('create/', views.faq_create, name='faq_create'),
    path('<int:pk>/update/', views.faq_update, name='faq_update'),
    path('<int:pk>/delete/', views.faq_delete, name='faq_delete'),
    path('toggle-status/', views.faq_toggle_status, name='faq_toggle_status'),
    path('update-order/', views.faq_update_order, name='faq_update_order'),
]