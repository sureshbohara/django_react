from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models import Q

from .models import Customer
from .forms import CustomerForm, CustomerEmailForm


@login_required
def customer_list(request):
    items = Customer.objects.all()
    
    if search := request.GET.get('search'):
        items = items.filter(Q(name__icontains=search) | Q(email__icontains=search) | Q(phone__icontains=search))
    if status := request.GET.get('status'):
        items = items.filter(is_active=bool(int(status)))
    
    paginator = Paginator(items, 15)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    return render(request, 'admin/customers/index.html', {
        'page_obj': page_obj,
        'filters': request.GET
    })


@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Customer created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/customers/form.html', {'form': CustomerForm()})


@login_required
def customer_update(request, pk):
    item = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Customer updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/customers/form.html', {'form': CustomerForm(instance=item), 'item': item})


@login_required
def customer_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Customer, pk=pk).delete()
    return redirect('customers:customer_list')


@login_required
def send_customer_email(request):
    if request.method == 'POST':
        form = CustomerEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message_html = form.cleaned_data['message']
            recipient_type = form.cleaned_data['recipient_type']
            
            if recipient_type == 'all':
                customers = Customer.objects.filter(is_active=True)
            else:
                customers = Customer.objects.filter(is_active=True, subscribed_to_newsletter=True)

            sent_count = 0
            for customer in customers:
                try:
                    html_content = render_to_string('emails/promotional_email.html', {
                        'customer_name': customer.name,
                        'message': message_html,
                        'site_name': 'Your Shop Name'
                    })
                    msg = EmailMultiAlternatives(
                        subject=subject,
                        body="Please view this email in a browser.",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        to=[customer.email]
                    )
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    sent_count += 1
                except Exception as e:
                    print(f"Failed to send to {customer.email}: {e}")

            return JsonResponse({'success': True, 'message': f'Email sent to {sent_count} customers!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    return render(request, 'admin/customers/send_email.html', {'form': CustomerEmailForm()})