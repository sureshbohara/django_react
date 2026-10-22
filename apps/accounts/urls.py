from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),


     # Profile & Password 
    path("profile/", views.show_profile, name="profile"),
    path("profile/update/", views.update_profile, name="profile_update"),
    path("change-password/", views.show_change_password, name="change_password"),
    path("change-password/update/", views.update_password, name="password_update"),

     # Admin Users CRUD
    path("admin-users/", views.admin_user_list, name="admin_user_list"),
    path("admin-users/create/", views.admin_user_create, name="admin_user_create"),
    path("admin-users/<int:pk>/update/", views.admin_user_update, name="admin_user_update"),
    path("admin-users/<int:pk>/delete/", views.admin_user_delete, name="admin_user_delete"),
    path("admin-users/toggle-status/", views.admin_user_toggle_status, name="admin_user_toggle_status"),
]