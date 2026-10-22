from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('create/', views.team_create, name='team_create'),
    path('<int:pk>/update/', views.team_update, name='team_update'),
    path('<int:pk>/delete/', views.team_delete, name='team_delete'),
    path('toggle-status/', views.team_toggle_status, name='team_toggle_status'),
    path('update-order/', views.team_update_order, name='team_update_order'),
]