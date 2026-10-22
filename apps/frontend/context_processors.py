from customers.models import Customer

def cart_count(request):
    cart = request.session.get('cart', {})
    total_items = sum(item['qty'] for item in cart.values())
    return {'cart_total_items': total_items}

def frontend_customer(request):
    customer_id = request.session.get('customer_id')
    if customer_id:
        try:
            return {'frontend_customer': Customer.objects.get(id=customer_id, is_active=True)}
        except Customer.DoesNotExist:
            if 'customer_id' in request.session:
                del request.session['customer_id']
    return {'frontend_customer': None}