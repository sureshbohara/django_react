from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import SiteSetting
from .forms import SiteSettingForm


def extract_dynamic_items(request):
    def extract_items(prefix):
        items = []
        idx = 0
        while f'{prefix}[{idx}][icon]' in request.POST or f'{prefix}[{idx}][title]' in request.POST:
            items.append({
                'icon': request.POST.get(f'{prefix}[{idx}][icon]', ''),
                'title': request.POST.get(f'{prefix}[{idx}][title]', ''),
                'subtitle': request.POST.get(f'{prefix}[{idx}][subtitle]', ''),
                'content': request.POST.get(f'{prefix}[{idx}][content]', ''),
            })
            idx += 1
        return items
    
    return (
        extract_items('process_item'),
        extract_items('work_item'),
        extract_items('counter_item')
    )


@login_required
def settings_view(request):
    setting = SiteSetting.get_instance()
    form = SiteSettingForm(instance=setting)
    return render(request, 'admin/site_settings/index.html', {'form': form, 'setting': setting})


@login_required
def settings_update(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)
    
    setting = SiteSetting.get_instance()
    form = SiteSettingForm(request.POST, request.FILES, instance=setting)
    
    if form.is_valid():
        updated = form.save(commit=False)
        updated.process_item, updated.work_item, updated.counter_item = extract_dynamic_items(request)
        updated.save()
        return JsonResponse({'success': True, 'message': 'Settings updated successfully!'})
    
    return JsonResponse({'success': False, 'errors': form.errors}, status=422)