from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from .models import LoginActivity

@login_required
def login_activity_list(request):
    activities = LoginActivity.objects.select_related('user').all()
    
    # Filters
    search = request.GET.get('search')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    device_type = request.GET.get('device_type')
    per_page = request.GET.get('per_page', 10)

    if search:
        activities = activities.filter(
            Q(user__username__icontains=search) | 
            Q(user__email__icontains=search) | 
            Q(ip_address__icontains=search) |
            Q(os__icontains=search) |
            Q(browser__icontains=search)
        )
    
    if from_date:
        activities = activities.filter(login_at__date__gte=from_date)
    if to_date:
        activities = activities.filter(login_at__date__lte=to_date)
        
    if device_type in ['desktop', 'mobile', 'tablet']:
        activities = activities.filter(device_type=device_type)

    # Pagination
    paginator = Paginator(activities, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin/site_settings/login_activities.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })

@login_required
def delete_login_activity(request, pk):
    if request.method == 'POST':
        get_object_or_404(LoginActivity, pk=pk).delete()
        return JsonResponse({'success': True, 'message': 'Activity deleted!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def bulk_delete_activities(request):
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            deleted_count, _ = LoginActivity.objects.filter(id__in=ids).delete()
            return JsonResponse({'success': True, 'message': f'{deleted_count} activities deleted!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    return JsonResponse({'success': False}, status=400)