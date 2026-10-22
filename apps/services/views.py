from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Service
from .forms import ServiceForm


def extract_json_data(request):
    """Helper to extract dynamic process items and highlights from POST data"""
    # Extract Process Items
    process_items = []
    idx = 0
    while f'process_item[{idx}][title]' in request.POST:
        process_items.append({
            'title': request.POST.get(f'process_item[{idx}][title]'),
            'content': request.POST.get(f'process_item[{idx}][content]')
        })
        idx += 1

    # Extract Highlight Sections
    highlight_sections = request.POST.getlist('highlight_sections[]')
    highlights = {'sections': highlight_sections} if highlight_sections else {}

    return process_items, highlights


@login_required
def service_list(request):
    items = Service.objects.all()
    
    if search := request.GET.get('search'):
        items = items.filter(title__icontains=search)
    if status := request.GET.get('status'):
        items = items.filter(status=bool(int(status)))
    
    paginator = Paginator(items, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/services/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.process_item, service.highlight = extract_json_data(request)
            service.save()
            return JsonResponse({'success': True, 'message': 'Service created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/services/form.html', {'form': ServiceForm()})


@login_required
def service_update(request, pk):
    item = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            service = form.save(commit=False)
            service.process_item, service.highlight = extract_json_data(request)
            service.save()
            return JsonResponse({'success': True, 'message': 'Service updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/services/form.html', {'form': ServiceForm(instance=item), 'item': item})


@login_required
def service_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Service, pk=pk).delete()
    return redirect('services:service_list')


@login_required
def service_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Service, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def service_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Service, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)