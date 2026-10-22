from django.urls import path
from . import views

app_name = 'login_activities'

urlpatterns = [
    path('', views.login_activity_list, name='list'),
    path('bulk-delete/', views.bulk_delete_activities, name='bulk_delete'),
    path('<int:pk>/delete/', views.delete_login_activity, name='delete'),
]