from django.core.management.base import BaseCommand
from pages.models import Page 

class Command(BaseCommand):
    help = 'Seeds E-commerce CMS Pages (Privacy, Terms, About, Shipping)'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding E-commerce CMS Pages...')

        pages_data = [
            {
                'title': 'Privacy Policy',
                'slug': 'privacy-policy',
                'icon': 'bi-shield-lock',
                'short_content': 'How we collect, use, and protect your personal information.',
                'content': '<h2>1. Information We Collect</h2><p>We collect information you provide directly to us, such as when you create an account, make a purchase, or contact us.</p><h2>2. How We Use Your Information</h2><p>We use the information to process your orders, communicate with you, and improve our services.</p><h2>3. Data Security</h2><p>We implement appropriate technical and organizational measures to protect your personal data.</p>',
                'meta_title': 'Privacy Policy - Caroline\'s House of Fragrances',
                'meta_description': 'Read our privacy policy to understand how we handle your data.',
                'show_in_menu': False,
                'show_in_footer': True,  
                'is_featured': False,
                'order_level': 10,
                'status': True,
            },
            {
                'title': 'Terms & Conditions',
                'slug': 'terms-and-conditions',
                'icon': 'bi-file-earmark-text',
                'short_content': 'The rules and guidelines for using our services and website.',
                'content': '<h2>1. Acceptance of Terms</h2><p>By accessing and using this website, you accept and agree to be bound by the terms and provision of this agreement.</p><h2>2. Booking and Payment</h2><p>All orders are subject to availability. Payment must be completed to confirm your reservation.</p><h2>3. Cancellation Policy</h2><p>Cancellations made before shipping will receive a full refund minus a small administrative fee.</p>',
                'meta_title': 'Terms & Conditions - Caroline\'s House of Fragrances',
                'meta_description': 'Our terms and conditions for purchasing beauty products.',
                'show_in_menu': False,
                'show_in_footer': True, 
                'is_featured': False,
                'order_level': 11,
                'status': True,
            },
            {
                'title': 'About Us',
                'slug': 'about-us',
                'icon': 'bi-info-circle',
                'short_content': 'Learn about our journey, mission, and the team behind our store.',
                'content': '<p>Caroline\'s House of Fragrances is a premier beauty and fragrance retailer. Founded by a group of passionate beauty enthusiasts, we are dedicated to providing authentic, high-quality, and sustainable beauty products.</p><p>We believe luxury should be pure, sustainable, and deeply personal. Every product in our collection is carefully curated to ensure it meets our high standards of quality and ethics.</p>',
                'meta_title': 'About Us - Caroline\'s House of Fragrances',
                'meta_description': 'Discover the story and mission behind our premium beauty store.',
                'show_in_menu': True,   
                'show_in_footer': True,
                'is_featured': True,
                'order_level': 1,
                'status': True,
            },
            {
                'title': 'Shipping & Returns',
                'slug': 'shipping-returns',
                'icon': 'bi-truck',
                'short_content': 'Our policies for shipping, delivery, and product returns.',
                'content': '<h2>Shipping</h2><p>We offer free standard shipping on all orders over Rs. 5000. Orders are typically processed within 1-2 business days.</p><h2>Returns</h2><p>If you are not completely satisfied with your purchase, you may return it within 14 days of receipt for a full refund. Products must be unused and in their original packaging.</p>',
                'meta_title': 'Shipping & Returns - Caroline\'s House of Fragrances',
                'meta_description': 'Learn about our shipping options and hassle-free return policy.',
                'show_in_menu': False,
                'show_in_footer': True,
                'is_featured': False,
                'order_level': 12,
                'status': True,
            }
        ]

        for page in pages_data:
            Page.objects.update_or_create(
                slug=page['slug'],
                defaults=page
            )

        self.stdout.write(self.style.SUCCESS('✅ CMS Pages seeded successfully!'))