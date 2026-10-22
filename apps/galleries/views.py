from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Gallery
from .forms import GalleryForm


@login_required
def gallery_list(request):
    items = Gallery.objects.all().order_by('order_level', '-created_at')
    
    # Filtering
    if search := request.GET.get('search'):
        items = items.filter(name__icontains=search)
    
    if display_on := request.GET.get('display_on'):
        items = items.filter(display_on=display_on)
    
    if status := request.GET.get('status'):
        items = items.filter(status=bool(int(status)))
    
    # Pagination
    paginator = Paginator(items, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/galleries/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def gallery_create(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Gallery image added successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/galleries/form.html', {'form': GalleryForm()})


@login_required
def gallery_update(request, pk):
    item = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Gallery image updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/galleries/form.html', {'form': GalleryForm(instance=item), 'item': item})


@login_required
def gallery_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Gallery, pk=pk).delete()
    return redirect('galleries:gallery_list')


@login_required
def gallery_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Gallery, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def gallery_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Gallery, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)