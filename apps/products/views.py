from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Product, ProductAttribute, ProductVariant, ProductBundle
from .forms import ProductForm, ProductAttributeForm, ProductVariantForm

from brands.models import Brand
from categories.models import Category


import os
from django.conf import settings
from django.utils.text import get_valid_filename

def extract_product_extras(request, is_update=False, instance=None):
    # 1. Extract FAQs
    faqs = []
    idx = 0
    while f'faqs[{idx}][question]' in request.POST:
        faqs.append({
            'question': request.POST.get(f'faqs[{idx}][question]'),
            'answer': request.POST.get(f'faqs[{idx}][answer]')
        })
        idx += 1

    # 2. Extract and Save Gallery Images Correctly
    gallery = list(instance.gallery) if (is_update and instance and instance.gallery) else []
    
    for file in request.FILES.getlist('gallery'):
        # Clean filename
        filename = get_valid_filename(file.name)
        # Define path relative to MEDIA_ROOT
        rel_path = os.path.join('products', 'gallery', filename)
        full_path = os.path.join(settings.MEDIA_ROOT, rel_path)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Save the file to disk
        with open(full_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
                
        # Append the correct URL to the gallery list
        gallery.append(f"{settings.MEDIA_URL}{rel_path}")

    # 3. Extract Bundle Products
    bundle_products = []
    b_idx = 0
    while f'bundle_products[{b_idx}][product_id]' in request.POST:
        bundle_products.append({
            'product_id': request.POST.get(f'bundle_products[{b_idx}][product_id]'),
            'quantity': request.POST.get(f'bundle_products[{b_idx}][quantity]')
        })
        b_idx += 1

    return faqs, gallery, bundle_products

# ==========================================
# PRODUCT CRUD
# ==========================================

@login_required
def product_list(request):
    items = Product.objects.select_related('brand', 'category').all()
    if search := request.GET.get('search'): items = items.filter(Q(name__icontains=search) | Q(sku__icontains=search))
    if product_type := request.GET.get('product_type'): items = items.filter(product_type=product_type)
    if status := request.GET.get('status'): items = items.filter(status=bool(int(status)))
    
    paginator = Paginator(items, 15)
    return render(request, 'admin/products/index.html', {'page_obj': paginator.get_page(request.GET.get('page')), 'filters': request.GET})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.faqs, product.gallery, bundle_data = extract_product_extras(request)
            product.save()
            for b in bundle_data:
                if b['product_id']: ProductBundle.objects.create(parent_product=product, child_product_id=b['product_id'], quantity=b['quantity'])
            return JsonResponse({'success': True, 'message': 'Product created!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    context = {
        'form': ProductForm(),
        'brands': Brand.objects.filter(status=True).order_by('name'),
        'categories': Category.objects.filter(parent__isnull=True).order_by('name'),
        'all_products': Product.objects.filter(status=True, product_type='simple').order_by('name')
    }
    return render(request, 'admin/products/form.html', context)

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.faqs, updated.gallery, bundle_data = extract_product_extras(request, is_update=True, instance=product)
            updated.save()
            product.bundle_items.all().delete()
            for b in bundle_data:
                if b['product_id']: ProductBundle.objects.create(parent_product=product, child_product_id=b['product_id'], quantity=b['quantity'])
            return JsonResponse({'success': True, 'message': 'Product updated!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    context = {
        'form': ProductForm(instance=product), 'item': product,
        'brands': Brand.objects.filter(status=True).order_by('name'),
        'categories': Category.objects.filter(parent__isnull=True).order_by('name'),
        'all_products': Product.objects.filter(status=True, product_type='simple').exclude(id=product.id).order_by('name')
    }
    return render(request, 'admin/products/form.html', context)

@login_required
def product_delete(request, pk):
    if request.method == 'POST': get_object_or_404(Product, pk=pk).delete()
    return redirect('products:product_list')

@login_required
def product_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Product, pk=request.POST.get('status_id'))
        item.status = not item.status; item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def product_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Product, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level')); item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)


# ==========================================
# ATTRIBUTE CRUD
# ==========================================

@login_required
def attribute_list(request):
    items = ProductAttribute.objects.all().order_by('order_level', '-created_at')
    if search := request.GET.get('search'): items = items.filter(name__icontains=search)
    if status := request.GET.get('status'): items = items.filter(status=bool(int(status)))
    paginator = Paginator(items, 15)
    return render(request, 'admin/products/attribute_index.html', {'page_obj': paginator.get_page(request.GET.get('page')), 'filters': request.GET})

@login_required
def attribute_create(request):
    if request.method == 'POST':
        form = ProductAttributeForm(request.POST)
        if form.is_valid():
            attr = form.save(commit=False)
            attr.values = request.POST.getlist('values[]')
            attr.save()
            return JsonResponse({'success': True, 'message': 'Attribute created!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/products/attribute_form.html', {'form': ProductAttributeForm()})

@login_required
def attribute_update(request, pk):
    item = get_object_or_404(ProductAttribute, pk=pk)
    if request.method == 'POST':
        form = ProductAttributeForm(request.POST, instance=item)
        if form.is_valid():
            attr = form.save(commit=False)
            attr.values = request.POST.getlist('values[]')
            attr.save()
            return JsonResponse({'success': True, 'message': 'Attribute updated!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/products/attribute_form.html', {'form': ProductAttributeForm(instance=item), 'item': item})

@login_required
def attribute_delete(request, pk):
    if request.method == 'POST': get_object_or_404(ProductAttribute, pk=pk).delete()
    return redirect('products:attribute_list')

@login_required
def attribute_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(ProductAttribute, pk=request.POST.get('status_id'))
        item.status = not item.status; item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def attribute_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(ProductAttribute, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level')); item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)


# ==========================================
# VARIANT CRUD
# ==========================================

@login_required
def variant_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    variants = ProductVariant.objects.filter(product=product)
    attributes = ProductAttribute.objects.filter(status=True).order_by('order_level')
    return render(request, 'admin/products/variant_list.html', {'product': product, 'variants': variants, 'attributes': attributes})

@login_required
def variant_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductVariantForm(request.POST, request.FILES)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.product = product
            variant.status = True 
            variant.save()
            return JsonResponse({'success': True, 'message': 'Variant created!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@login_required
def variant_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(ProductVariant, pk=pk).delete()
        return JsonResponse({'success': True, 'message': 'Variant deleted!'})
    return JsonResponse({'success': False}, status=400)