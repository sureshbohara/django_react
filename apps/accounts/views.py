from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from .models import AdminUser
from .forms import ProfileForm, ChangePasswordForm, AdminUserForm

from login_activities.utils import record_login_activity, record_logout_activity

# ─── Auth Views ──────────────────────
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated: 
            return redirect("core:dashboard")
        return render(request, "admin/accounts/login.html")

    def post(self, request):
        email, password = request.POST.get("email"), request.POST.get("password")
        try:
            admin = AdminUser.objects.get(email=email)
            if not admin.status: 
                return JsonResponse({"success": False, "errors": {"email": ["Account is inactive."]}}, status=403)
        except AdminUser.DoesNotExist:
            return JsonResponse({"success": False, "errors": {"email": ["Account not found."]}}, status=403)

        user = authenticate(request, email=email, password=password)
        if user is None: 
            return JsonResponse({"success": False, "errors": {"password": ["Incorrect password."]}}, status=401)

        login(request, user)

        record_login_activity(user, request)

        if not request.POST.get("remember") == "1": 
            request.session.set_expiry(0)
        return JsonResponse({"success": True, "message": "Login successful!", "redirect": "/dashboard/"})


class LogoutView(View):
    def post(self, request):


        if request.user.is_authenticated:
            record_logout_activity(request.user)
            
        logout(request)
        return redirect("accounts:login")




# ─── Profile & Password Views ──────────────────────
@login_required
def show_profile(request):
    form = ProfileForm(instance=request.user)
    return render(request, "admin/accounts/profile.html", {"form": form, "admin": request.user})

@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            saved_user = form.save()
            return JsonResponse({"success": True, "message": "Profile updated successfully!", "image_url": saved_user.image_url})
        return JsonResponse({"success": False, "errors": form.errors}, status=422)
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)


@login_required
def show_change_password(request):
    form = ChangePasswordForm()
    return render(request, "admin/accounts/change_password.html", {"form": form, "admin": request.user})

@login_required
def update_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data["current_password"]
            new_password = form.cleaned_data["password"]
            if not request.user.check_password(current_password):
                return JsonResponse({"success": False, "errors": {"current_password": ["Current password is incorrect."]}}, status=422)
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            return JsonResponse({"success": True, "message": "Password updated successfully!"})
        return JsonResponse({"success": False, "errors": form.errors}, status=422)
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)



# ─── Admin Users CRUD Views ──────────────────────
@login_required
def admin_user_list(request):
    users = AdminUser.objects.all()
    if request.GET.get("search"): 
        users = users.filter(Q(name__icontains=request.GET.get("search")) | Q(email__icontains=request.GET.get("search")))
    if request.GET.get("status") in ["0", "1"]: 
        users = users.filter(status=bool(int(request.GET.get("status"))))
    return render(request, "admin/accounts/admin_users/index.html", {"items": users, "filters": request.GET})


@login_required
def admin_user_create(request):
    if request.method == "POST":
        form = AdminUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if request.POST.get("password"): user.set_password(request.POST.get("password"))
            user.save()
            return JsonResponse({"success": True, "message": "Admin user created successfully!"})
        return JsonResponse({"success": False, "errors": form.errors}, status=422)
    return render(request, "admin/accounts/admin_users/form.html", {"form": AdminUserForm()})


@login_required
def admin_user_update(request, pk):
    user = get_object_or_404(AdminUser, pk=pk)
    if request.method == "POST":
        form = AdminUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)
            if request.POST.get("password"): updated_user.set_password(request.POST.get("password"))
            updated_user.save()
            return JsonResponse({"success": True, "message": "Admin user updated successfully!"})
        return JsonResponse({"success": False, "errors": form.errors}, status=422)
    return render(request, "admin/accounts/admin_users/form.html", {"form": AdminUserForm(instance=user), "item": user})


@login_required
def admin_user_delete(request, pk):
    if request.method == "POST": 
        get_object_or_404(AdminUser, pk=pk).delete()
    return redirect("accounts:admin_user_list")


@login_required
def admin_user_toggle_status(request):
    if request.method == "POST":
        user = get_object_or_404(AdminUser, pk=request.POST.get("status_id"))
        user.status = not user.status
        user.save()
        return JsonResponse({"success": True, "message": "User status updated!"})
    return JsonResponse({"success": False}, status=400)