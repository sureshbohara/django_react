from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Order
from .forms import OrderStatusForm

@login_required
def order_list(request):
    orders = Order.objects.select_related('customer').all()
    
    if search := request.GET.get('search'):
        orders = orders.filter(Q(order_number__icontains=search) | Q(shipping_name__icontains=search) | Q(shipping_phone__icontains=search))
    if status := request.GET.get('status'):
        orders = orders.filter(status=status)
        
    paginator = Paginator(orders, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/orders/index.html', {'page_obj': page_obj, 'filters': request.GET})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Order status updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    form = OrderStatusForm(instance=order)
    return render(request, 'admin/orders/detail.html', {'order': order, 'form': form})