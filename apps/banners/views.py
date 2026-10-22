from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Banner
from .forms import BannerForm


# ═══════════════════════════════════════════════════════════════
# 1. LIST VIEW (Filter + Pagination)
# ═══════════════════════════════════════════════════════════════
@login_required
def banner_list(request):
    # Base query
    banners = Banner.objects.all().order_by('order_level', '-created_at')
    
    # Filtering 
    if title := request.GET.get('title'):
        banners = banners.filter(title__icontains=title)
    
    if status := request.GET.get('status'):
        banners = banners.filter(status=bool(int(status)))
    
    # Pagination 
    paginator = Paginator(banners, 15)  
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/banners/index.html', {
        'page_obj': page_obj,  
        'filters': request.GET
    })


# ═══════════════════════════════════════════════════════════════
# 2. CREATE VIEW
# ═══════════════════════════════════════════════════════════════
@login_required
def banner_create(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True, 
                'message': 'Banner created successfully!'
            })
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    return render(request, 'admin/banners/form.html', {'form': BannerForm()})


# ═══════════════════════════════════════════════════════════════
# 3. UPDATE VIEW
# ═══════════════════════════════════════════════════════════════
@login_required
def banner_update(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True, 
                'message': 'Banner updated successfully!'
            })
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    return render(request, 'admin/banners/form.html', {
        'form': BannerForm(instance=banner), 
        'banner': banner
    })


# ═══════════════════════════════════════════════════════════════
# 4. DELETE VIEW
# ═══════════════════════════════════════════════════════════════
@login_required
def banner_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Banner, pk=pk).delete()
    return redirect('banners:banner_list')


# ═══════════════════════════════════════════════════════════════
# 5. AJAX: TOGGLE STATUS
# ═══════════════════════════════════════════════════════════════
@login_required
def banner_toggle_status(request):
    if request.method == 'POST':
        banner = get_object_or_404(Banner, pk=request.POST.get('status_id'))
        banner.status = not banner.status
        banner.save()
        return JsonResponse({
            'success': True, 
            'message': 'Status updated!'
        })
    return JsonResponse({'success': False}, status=400)


# ═══════════════════════════════════════════════════════════════
# 6. AJAX: UPDATE ORDER LEVEL
# ═══════════════════════════════════════════════════════════════
@login_required
def banner_update_order(request):
    if request.method == 'POST':
        banner = get_object_or_404(Banner, pk=request.POST.get('id'))
        banner.order_level = int(request.POST.get('order_level'))
        banner.save()
        return JsonResponse({
            'success': True, 
            'message': 'Order updated!'
        })
    return JsonResponse({'success': False}, status=400)