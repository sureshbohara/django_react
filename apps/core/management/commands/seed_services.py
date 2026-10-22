from django.core.management.base import BaseCommand
from services.models import Service  

class Command(BaseCommand):
    help = 'Seeds the Service table with default travel services'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Services...')

        services_data = [
            {
                'title': 'Airport Transfer',
                'subtitle': 'Reliable 24/7 Pickup and Drop-off',
                'icon': 'bi-airplane',
                'short_content': 'Start your journey stress-free with our comfortable and punctual airport transfer service.',
                'long_content': 'Our professional drivers will be waiting for you at Tribhuvan International Airport with a name board. We provide safe, air-conditioned vehicles for a smooth ride to your hotel.',
                'slug': 'airport-transfer',
                'image': None,        
                'feature_image': None,  
                'process_title': 'How it Works',
                'process_sub_title': 'Simple 3-step process',
                'process_item': [
                    {'step': '1', 'title': 'Book Online', 'desc': 'Provide your flight details and hotel name.'},
                    {'step': '2', 'title': 'Meet Driver', 'desc': 'Our driver will meet you at the arrival gate.'},
                    {'step': '3', 'title': 'Enjoy Ride', 'desc': 'Relax and enjoy a comfortable ride to your destination.'}
                ],
                'highlight': {'title': 'Why Choose Us?', 'points': ['24/7 Availability', 'Free Flight Monitoring', 'Fixed Prices']},
                'order_level': 1,
                'status': True,
            },
            {
                'title': 'Visa Assistance',
                'subtitle': 'Hassle-free Nepal and Tibet Visa Processing',
                'icon': 'bi-passport',
                'short_content': 'Let us handle the paperwork while you focus on your adventure.',
                'long_content': 'We provide complete guidance and support for obtaining your Nepal Tourist Visa on Arrival or Tibet Travel Permit, ensuring a smooth entry process.',
                'slug': 'visa-assistance',
                'image': None,
                'feature_image': None,
                'process_title': 'Visa Process',
                'process_sub_title': 'We make it easy',
                'process_item': [
                    {'step': '1', 'title': 'Share Documents', 'desc': 'Send us a copy of your passport.'},
                    {'step': '2', 'title': 'We Process', 'desc': 'Our team handles the application and fees.'},
                    {'step': '3', 'title': 'Get Approved', 'desc': 'Receive your visa/permit before travel.'}
                ],
                'highlight': {'title': 'Guaranteed', 'points': ['Fast Processing', 'Expert Guidance', 'Document Safety']},
                'order_level': 2,
                'status': True,
            }
        ]

        for service in services_data:
            Service.objects.update_or_create(
                slug=service['slug'],
                defaults=service
            )

        self.stdout.write(self.style.SUCCESS('✅ Services seeded successfully!'))