from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Review
from .forms import ReviewForm


@login_required
def review_list(request):
    items = Review.objects.all()

    # Filtering
    if search := request.GET.get('search'):
        items = items.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search) |
            Q(review__icontains=search)
        )

    if display_on := request.GET.get('display_on'):
        items = items.filter(display_on=display_on)

    if rating := request.GET.get('rating'):
        items = items.filter(rating=int(rating))

    if status := request.GET.get('status'):
        items = items.filter(status=bool(int(status)))

    # Pagination
    paginator = Paginator(items, 15)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'admin/reviews/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Review created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/reviews/form.html', {'form': ReviewForm()})


@login_required
def review_update(request, pk):
    item = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Review updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/reviews/form.html', {
        'form': ReviewForm(instance=item),
        'item': item
    })


@login_required
def review_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Review, pk=pk).delete()
    return redirect('reviews:review_list')


@login_required
def review_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Review, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def review_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Review, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)