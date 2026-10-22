from django.core.management.base import BaseCommand
from coupons.models import Coupon
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seeds E-commerce Coupons with realistic discount scenarios'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding E-commerce Coupons...')

        today = datetime.now().date()

        coupons_data = [
            {
                'code': 'WELCOME15',
                'description': 'Get 15% off your first order! Welcome to Caroline\'s House.',
                'discount_type': 'percentage',
                'discount_value': 15.00,
                'min_order_amount': 1000.00,
                'max_discount': 500.00,  
                'usage_limit': None,     
                'usage_limit_per_user': 1,
                'start_date': today,
                'end_date': today + timedelta(days=365),
                'status': True,
            },
            {
                'code': 'SAVE500',
                'description': 'Flat Rs. 500 off on orders above Rs. 5000',
                'discount_type': 'fixed',
                'discount_value': 500.00,
                'min_order_amount': 5000.00,
                'max_discount': None,
                'usage_limit': 100,
                'usage_limit_per_user': 2,
                'start_date': today,
                'end_date': today + timedelta(days=90),
                'status': True,
            },
            {
                'code': 'FLASH20',
                'description': 'Weekend Flash Sale: 20% off on all luxury perfumes',
                'discount_type': 'percentage',
                'discount_value': 20.00,
                'min_order_amount': 2000.00,
                'max_discount': 1000.00,
                'usage_limit': 50,      
                'usage_limit_per_user': 1,
                'start_date': today,
                'end_date': today + timedelta(days=7),
                'status': True,
            },
            {
                'code': 'FREESHIP',
                'description': 'Free Shipping on all orders (Rs. 150 discount)',
                'discount_type': 'fixed',
                'discount_value': 150.00, 
                'min_order_amount': 0.00,
                'max_discount': None,
                'usage_limit': None,
                'usage_limit_per_user': 5,
                'start_date': today,
                'end_date': today + timedelta(days=180),
                'status': True,
            },
            {
                'code': 'VIP30',
                'description': 'Exclusive 30% discount for our VIP members',
                'discount_type': 'percentage',
                'discount_value': 30.00,
                'min_order_amount': 10000.00,
                'max_discount': 3000.00,
                'usage_limit': 20,      
                'usage_limit_per_user': 1,
                'start_date': today,
                'end_date': today + timedelta(days=30),
                'status': True,
            },
            {
                'code': 'EXPIRED10',
                'description': 'This is an expired coupon for testing frontend validation',
                'discount_type': 'percentage',
                'discount_value': 10.00,
                'min_order_amount': 0.00,
                'max_discount': None,
                'usage_limit': 100,
                'usage_limit_per_user': 1,
                'start_date': today - timedelta(days=60),
                'end_date': today - timedelta(days=30), 
                'status': True, 
            },
            {
                'code': 'INACTIVE50',
                'description': 'This coupon is manually disabled by admin',
                'discount_type': 'fixed',
                'discount_value': 50.00,
                'min_order_amount': 0.00,
                'max_discount': None,
                'usage_limit': None,
                'usage_limit_per_user': 1,
                'start_date': today,
                'end_date': today + timedelta(days=365),
                'status': False,
            },
        ]

        for coupon_data in coupons_data:
            Coupon.objects.update_or_create(
                code=coupon_data['code'],
                defaults=coupon_data
            )
            self.stdout.write(f"  ✅ Created/Updated: {coupon_data['code']} ({coupon_data['discount_type']} {coupon_data['discount_value']})")

        self.stdout.write(self.style.SUCCESS('🚀 E-commerce Coupons seeded successfully!'))