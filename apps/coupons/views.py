from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Coupon
from .forms import CouponForm


@login_required
def coupon_list(request):
    coupons = Coupon.objects.all()
    
    # Filtering
    if code := request.GET.get('code'):
        coupons = coupons.filter(code__icontains=code)
    
    if discount_type := request.GET.get('discount_type'):
        coupons = coupons.filter(discount_type=discount_type)
    
    if status := request.GET.get('status'):
        coupons = coupons.filter(status=bool(int(status)))
    
    # Pagination
    paginator = Paginator(coupons, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/coupons/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def coupon_create(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            coupon = form.save(commit=False)
            coupon.code = coupon.code.upper().strip()
            coupon.save()
            return JsonResponse({'success': True, 'message': 'Coupon created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/coupons/form.html', {'form': CouponForm()})


@login_required
def coupon_update(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    if request.method == 'POST':
        form = CouponForm(request.POST, instance=coupon)
        if form.is_valid():
            updated_coupon = form.save(commit=False)
            updated_coupon.code = updated_coupon.code.upper().strip()
            updated_coupon.save()
            return JsonResponse({'success': True, 'message': 'Coupon updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/coupons/form.html', {
        'form': CouponForm(instance=coupon),
        'coupon': coupon
    })


@login_required
def coupon_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Coupon, pk=pk).delete()
    return redirect('coupons:coupon_list')


@login_required
def coupon_toggle_status(request):
    if request.method == 'POST':
        coupon = get_object_or_404(Coupon, pk=request.POST.get('status_id'))
        coupon.status = not coupon.status
        coupon.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def coupon_reset_usage(request):
    if request.method == 'POST':
        coupon = get_object_or_404(Coupon, pk=request.POST.get('id'))
        coupon.used_count = 0
        coupon.save()
        return JsonResponse({'success': True, 'message': 'Usage count reset!'})
    return JsonResponse({'success': False}, status=400)