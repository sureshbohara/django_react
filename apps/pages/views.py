from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Page
from .forms import PageForm


@login_required
def page_list(request):
    items = Page.objects.all()
    
    # Filtering
    if search := request.GET.get('search'):
        items = items.filter(title__icontains=search)
    
    if show_in_menu := request.GET.get('show_in_menu'):
        items = items.filter(show_in_menu=bool(int(show_in_menu)))
    
    if show_in_footer := request.GET.get('show_in_footer'):
        items = items.filter(show_in_footer=bool(int(show_in_footer)))
    
    if is_featured := request.GET.get('is_featured'):
        items = items.filter(is_featured=bool(int(is_featured)))
    
    if status := request.GET.get('status'):
        items = items.filter(status=bool(int(status)))
    
    # Pagination
    paginator = Paginator(items, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/pages/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Page created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/pages/form.html', {'form': PageForm()})


@login_required
def page_update(request, pk):
    item = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Page updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/pages/form.html', {'form': PageForm(instance=item), 'item': item})


@login_required
def page_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Page, pk=pk).delete()
    return redirect('pages:page_list')


@login_required
def page_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Page, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def page_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Page, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)