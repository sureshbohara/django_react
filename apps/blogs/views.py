from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm


@login_required
def post_list(request):
    # Base query
    posts = Post.objects.select_related('category').all().order_by('order_level', '-created_at')
    # Filtering
    if search := request.GET.get('search'):
        posts = posts.filter(title__icontains=search)
    if status := request.GET.get('status'):
        posts = posts.filter(status=bool(int(status)))
    
    # Pagination 
    paginator = Paginator(posts, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/blogs/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Blog post created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/blogs/form.html', {'form': PostForm()})


@login_required
def post_update(request, pk):
    item = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Blog post updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/blogs/form.html', {'form': PostForm(instance=item), 'item': item})


@login_required
def post_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Post, pk=pk).delete()
    return redirect('blogs:post_list')


@login_required
def post_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Post, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def post_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Post, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)