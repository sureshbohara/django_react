from django.core.management.base import BaseCommand
from site_settings.models import SiteSetting 
from datetime import datetime

class Command(BaseCommand):
    help = 'Seeds the Site Settings with E-commerce default configuration'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding E-commerce Site Settings...')

        current_year = datetime.now().year

        SiteSetting.objects.update_or_create(
            pk=1, 
            defaults={
                # --- General Info ---
                'system_name': 'Caroline\'s House of Fragrances',
                'email': 'support@carolineshouse.com',
                'extra_email': 'booking@carolineshouse.com',
                'phone': '+977 9709065971',
                'extra_phone': '+977-1-XXXXXXX', 
                'address': '5 Plant Ave, Hauppauge, NY / Kathmandu, Nepal',
                'opening_hr': 'Sun - Fri: 9AM - 6PM',
                'work_hours': 'Your gateway to authentic luxury and beauty.',
                'footer_copyright': f'© {current_year} Caroline\'s House of Fragrances. All Rights Reserved.',
                'google_map': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3532.0284987496536!2d85.32405831506056!3d27.717245933190117!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39eb19a8b5b88e43%3A0x6d64b8f8b8b8b8b8!2sKathmandu!5e0!3m2!1sen!2snp!4v1620000000000', 

                # --- Social Links ---
                'facebook': 'https://facebook.com/carolineshouse',
                'twitter': 'https://twitter.com/carolineshouse',
                'linkedin': 'https://linkedin.com/company/carolineshouse',
                'instagram': 'https://instagram.com/carolineshouse',
                'youtube': 'https://youtube.com/@carolineshouse',
                'google': None,
                'yelp': None,

                # --- Media ---
                'favicon': None,
                'logo': None,
                'loader': None,
                'footer_gateway_img': None,
                'bg_image': None,
                'breadcrumb': None,
                'image1': None, 
                'image2': None,

                # --- SEO Meta Data ---
                'meta_author': 'Caroline\'s House of Fragrances',
                'meta_title': 'Caroline\'s House of Fragrances | Premium Perfumes & Skincare',
                'meta_keywords': 'perfume nepal, luxury skincare, makeup, beauty products, caroline house, organic beauty',
                'meta_description': 'Discover authentic luxury fragrances, premium skincare, and high-quality makeup at Caroline\'s House of Fragrances. Free shipping on orders over Rs. 5000.',

                # --- Info Texts ---
                'info1': 'Our Story',
                'info2': 'Each signature scent starts with a color and a feeling.',
                'info3': 'Caroline\'s House of Fragrances is a modern artisanal perfumery committed to producing high-quality products using ethically sourced, all-natural ingredients. We believe luxury should be pure, sustainable, and deeply personal.',
                'info4': 'Every product is made in small batches by hand, using only premium organic oils and botanicals. Pure, fresh luxury crafted just for you.',
                'info5': 'Secure Online Payments',
                'info6': '24/7 Customer Support',
                'info7': '100% Authentic Products',

                # --- SMTP / Mail ---
                'mail_transport': 'smtp',
                'mail_host': 'smtp.gmail.com',
                'mail_port': 587, 
                'mail_username': 'your_email@gmail.com',
                'mail_password': 'your_app_password',
                'mail_encryption': 'tls',
                'mail_from': 'noreply@carolineshouse.com',
                'mail_from_name': 'Caroline\'s House of Fragrances',
                'smtp_check': True,

                # --- ReCaptcha ---
                'recaptcha_site_key': '', 
                'recaptcha_secret_key': '', 
                'is_recaptcha': False,

                # --- Analytics ---
                'google_analytic_id': '',
                'facebook_analytic_id': '',

                # --- Social Login ---
                'facebook_client_id': '',
                'facebook_client_secret': '',
                'facebook_redirect': '',
                'is_facebook': False,
                'google_client_id': '',
                'google_client_secret': '',
                'google_redirect': '',
                'is_google': False,

            
                'process_title': 'Our Services',
                'process_sub_title': 'Why choose Caroline\'s House of Fragrances',
                'process_item': [
                    {
                        'icon': 'bi bi-truck', 
                        'title': 'Same Day Free Shipping', 
                        'content': 'Orders ship on the day that you place them.'
                    },
                    {
                        'icon': 'bi bi-shield-check', 
                        'title': 'Trusted Since 2001', 
                        'content': '100% authentic fragrances. No knockoffs.'
                    },
                    {
                        'icon': 'bi bi-lock-fill', 
                        'title': 'Safe & Secure Checkout', 
                        'content': 'Your information is 100% protected.'
                    },
                    {
                        'icon': 'bi bi-star-fill', 
                        'title': '5 Star Customer Ratings', 
                        'content': 'Over 20 million satisfied customers.'
                    }
                ],

                'work_title': 'Join Our Affiliate Program',
                'work_sub_title': 'Earn commissions by sharing your favorite beauty products with your audience.',
                'work_item': [
                    {'icon': 'bi bi-person-plus', 'title': 'Sign Up', 'content': 'Create an account and apply for our affiliate program.'},
                    {'icon': 'bi bi-link-45deg', 'title': 'Get Your Links', 'content': 'Receive unique tracking links for your favorite products.'},
                    {'icon': 'bi bi-share', 'title': 'Share & Promote', 'content': 'Share your links on your blog, social media, or website.'},
                    {'icon': 'bi bi-cash-coin', 'title': 'Earn Commissions', 'content': 'Get paid for every successful sale generated through your links.'}
                ],

                'counter_title': 'Why Shop With Us',
                'counter_sub_title': 'Trusted by Beauty Enthusiasts Across the Globe',
                'counter_item': [
                    {
                        'icon': 'bi bi-shield-lock-fill', 
                        'title': 'Safe & Secure', 
                        'content': '100% Protected Checkout'
                    },
                    {
                        'icon': 'bi bi-patch-check-fill', 
                        'title': '100% Authentic', 
                        'content': 'Genuine Fragrances Only'
                    },
                    {
                        'icon': 'bi bi-truck', 
                        'title': 'Same Day Shipping', 
                        'content': 'Orders dispatched daily'
                    },
                    {
                        'icon': 'bi bi-headset', 
                        'title': 'Expert Support', 
                        'content': 'Dedicated fragrance consultants'
                    }
                ],
            }
        )

        self.stdout.write(self.style.SUCCESS('✅ Site Settings seeded successfully!'))