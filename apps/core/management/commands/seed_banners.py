from django.core.management.base import BaseCommand
from banners.models import Banner

class Command(BaseCommand):
    help = 'Seeds E-commerce Hero Banners'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding E-commerce Banners...')

        banners_data = [
            {
                'title': 'Premium Perfumes Collection',
                'subtitle': 'Discover your signature scent from the world\'s most luxurious brands.',
                'description': 'Enjoy free shipping on all orders over Rs. 5000.',
                'order_level': 1,
                'status': True,
            },
            {
                'title': 'Luxury Skincare Essentials',
                'subtitle': 'Radiant, healthy skin starts here. Up to 40% off on selected serums.',
                'description': 'Clinically proven formulas for every skin type.',
                'order_level': 2,
                'status': True,
            },
            {
                'title': 'Exclusive Summer Sale',
                'subtitle': 'Refresh your makeup bag with our new summer arrivals.',
                'description': 'Use code SUMMER20 for an extra 20% off at checkout.',
                'order_level': 3,
                'status': True,
            }
        ]

        for banner_data in banners_data:
            Banner.objects.update_or_create(
                title=banner_data['title'],
                defaults=banner_data
            )
            self.stdout.write(f"  ✅ Created/Updated: {banner_data['title']}")

        self.stdout.write(self.style.SUCCESS('✅ Banners seeded successfully!'))