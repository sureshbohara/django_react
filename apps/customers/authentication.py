from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from customers.models import Customer

class CustomerJWTAuthentication(BaseAuthentication):
    """
    Mobile App ko Customer Token verify garne Custom Authentication.
    Yasle AdminUser lai touch gardaina, sidhai Customer table ma check garcha.
    """
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return None
            
        token_string = auth_header.split(' ')[1]
        
        try:
            # Token decode garne
            payload = jwt.decode(token_string, settings.SECRET_KEY, algorithms=['HS256'])
            customer_id = payload.get('customer_id')
            
            if not customer_id:
                return None
                
            # Customer table bata user nikalne
            customer = Customer.objects.get(id=customer_id, is_active=True)
            return (customer, token_string) # (user, auth_token)
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        except Customer.DoesNotExist:
            raise AuthenticationFailed('Customer not found')