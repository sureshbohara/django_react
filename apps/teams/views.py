from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Team
from .forms import TeamForm


@login_required
def team_list(request):
    items = Team.objects.all().order_by('order_level', 'name')
    
    if search := request.GET.get('search'):
        items = items.filter(name__icontains=search)
    if role := request.GET.get('role'):
        items = items.filter(role__icontains=role)
    if status := request.GET.get('status'):
        items = items.filter(status=bool(int(status)))
    
    paginator = Paginator(items, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/teams/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Team member added successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/teams/form.html', {'form': TeamForm()})


@login_required
def team_update(request, pk):
    item = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Team member updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/teams/form.html', {
        'form': TeamForm(instance=item), 
        'item': item
    })


@login_required
def team_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Team, pk=pk).delete()
    return redirect('teams:team_list')


@login_required
def team_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Team, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)


@login_required
def team_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Team, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)