from user_agents import parse
from .models import LoginActivity
from django.utils import timezone

def get_device_type(user_agent_string):
    ua = parse(user_agent_string)
    if ua.is_mobile:
        return 'mobile'
    elif ua.is_tablet:
        return 'tablet'
    return 'desktop'

def record_login_activity(user, request):
    ua_string = request.META.get('HTTP_USER_AGENT', '')
    ua = parse(ua_string)
    
    LoginActivity.objects.create(
        user=user,
        ip_address=get_client_ip(request),
        user_agent=ua_string,
        os=ua.os.family if ua.os.family else 'Unknown',
        browser=ua.browser.family if ua.browser.family else 'Unknown',
        device_type=get_device_type(ua_string),
    )

def record_logout_activity(user):

    active_session = LoginActivity.objects.filter(
        user=user, 
        logout_at__isnull=True
    ).order_by('-login_at').first()
    
    if active_session:
        active_session.logout_at = timezone.now()
        active_session.save()

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip