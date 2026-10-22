from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Category
from .forms import CategoryForm


@login_required
def category_list(request):
    categories = Category.objects.all().order_by('order_level', 'name')
    
    # Filtering
    if name := request.GET.get('name'):
        categories = categories.filter(name__icontains=name)
    
    if parent_id := request.GET.get('parent_id'):
        categories = categories.filter(parent_id=parent_id)
    
    if display_on := request.GET.get('display_on'):
        categories = categories.filter(display_on=display_on)
    
    if status := request.GET.get('status'):
        categories = categories.filter(status=bool(int(status)))
    
    # Pagination
    paginator = Paginator(categories, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    # Parent categories (search form  dropdown)
    parent_categories = Category.objects.filter(parent__isnull=True).order_by('name')
    
    return render(request, 'admin/categories/index.html', {
        'page_obj': page_obj,
        'parent_categories': parent_categories,
        'filters': request.GET
    })


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Category created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/categories/form.html', {'form': CategoryForm()})


@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Category updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/categories/form.html', {
        'form': CategoryForm(instance=category), 
        'category': category
    })


@login_required
def category_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Category, pk=pk).delete()
    return redirect('categories:category_list')


@login_required
def category_toggle_status(request):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=request.POST.get('status_id'))
        category.status = not category.status
        category.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def category_update_order(request):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=request.POST.get('id'))
        category.order_level = int(request.POST.get('order_level'))
        category.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)