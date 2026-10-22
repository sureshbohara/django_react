from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Brand
from .forms import BrandForm


@login_required
def brand_list(request):
    brands = Brand.objects.all().order_by('order_level', 'name')
    
    # Filtering
    if name := request.GET.get('name'):
        brands = brands.filter(name__icontains=name)
    if status := request.GET.get('status'):
        brands = brands.filter(status=bool(int(status)))
    
    # Pagination
    paginator = Paginator(brands, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/brands/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Brand created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/brands/form.html', {'form': BrandForm()})


@login_required
def brand_update(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Brand updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/brands/form.html', {'form': BrandForm(instance=brand), 'brand': brand})


@login_required
def brand_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Brand, pk=pk).delete()
    return redirect('brands:brand_list')


@login_required
def brand_toggle_status(request):
    if request.method == 'POST':
        brand = get_object_or_404(Brand, pk=request.POST.get('status_id'))
        brand.status = not brand.status
        brand.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def brand_update_order(request):
    if request.method == 'POST':
        brand = get_object_or_404(Brand, pk=request.POST.get('id'))
        brand.order_level = int(request.POST.get('order_level'))
        brand.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)