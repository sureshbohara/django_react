from django.core.management.base import BaseCommand
from faqs.models import Faq  

class Command(BaseCommand):
    help = 'Seeds E-commerce FAQs with realistic questions and answers'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding E-commerce FAQs...')

        faqs_data = [
       
            {
                'display_on': 'default',
                'question': 'How long does shipping take?',
                'answer': 'We process all orders within 1-2 business days. Standard delivery within Kathmandu Valley takes 1-2 days, while delivery to other parts of Nepal takes 3-5 business days.',
                'order_level': 1,
                'status': True,
            },
            {
                'display_on': 'default',
                'question': 'Do you offer free shipping?',
                'answer': 'Yes! We offer free standard shipping on all orders over Rs. 5,000. For orders below this amount, a flat shipping fee of Rs. 150 applies.',
                'order_level': 2,
                'status': True,
            },
            {
                'display_on': 'default',
                'question': 'How can I track my order?',
                'answer': 'Once your order is dispatched, you will receive an email and SMS with a tracking number. You can also track your order status by logging into your account and visiting the "My Orders" section.',
                'order_level': 3,
                'status': True,
            },

            # --- Returns & Refunds ---
            {
                'display_on': 'default',
                'question': 'What is your return and refund policy?',
                'answer': 'We accept returns within 7 days of delivery if the product is unused, unopened, and in its original packaging. Once we receive and inspect the item, we will process your refund within 5-7 business days.',
                'order_level': 4,
                'status': True,
            },
            {
                'display_on': 'default',
                'question': 'Can I return a perfume if I don\'t like the scent?',
                'answer': 'For hygiene and safety reasons, we cannot accept returns on opened or used perfumes and skincare products. However, if the product is defective or damaged upon arrival, we will gladly replace it or issue a full refund.',
                'order_level': 5,
                'status': True,
            },

            # --- Products & Authenticity ---
            {
                'display_on': 'default',
                'question': 'Are your products 100% authentic?',
                'answer': 'Absolutely. We source all our fragrances, skincare, and makeup products directly from authorized distributors and brands. We guarantee 100% authenticity and do not sell any counterfeit or replica items.',
                'order_level': 6,
                'status': True,
            },
            {
                'display_on': 'default',
                'question': 'Are your skincare products cruelty-free and vegan?',
                'answer': 'We are proud to offer a wide range of cruelty-free and vegan products. You can identify these items by the "Cruelty-Free" or "Vegan" badge on the product page. Please check individual product descriptions for specific details.',
                'order_level': 7,
                'status': True,
            },
            {
                'display_on': 'default',
                'question': 'Do perfumes have an expiration date?',
                'answer': 'Yes, perfumes typically have a shelf life of 3 to 5 years from the date of manufacture. To maximize their longevity, store them in a cool, dry place away from direct sunlight and extreme temperature changes.',
                'order_level': 8,
                'status': True,
            },

            # --- Account & Orders ---
            {
                'display_on': 'account',
                'question': 'Can I change or cancel my order after placing it?',
                'answer': 'You can cancel or modify your order within 2 hours of placing it. Please contact our customer support team immediately at support@carolineshouse.com or call +977 9709065971. Once an order is shipped, it cannot be canceled.',
                'order_level': 9,
                'status': True,
            },
            {
                'display_on': 'default',
                'question': 'Do you offer gift wrapping services?',
                'answer': 'Yes! We offer complimentary luxury gift wrapping for all orders. You can select the "Gift Wrap" option at checkout and even add a personalized message for the recipient.',
                'order_level': 10,
                'status': True,
            },
            {
                'display_on': 'account',
                'question': 'How do I create an account or reset my password?',
                'answer': 'You can create an account by clicking the "Login" icon at the top right of our homepage and selecting "Create an Account". If you forgot your password, click "Forgot Password" on the login page, and we will send you a reset link via email.',
                'order_level': 11,
                'status': True,
            },
        ]

        for faq in faqs_data:
            Faq.objects.update_or_create(
                question=faq['question'],
                defaults=faq
            )
            self.stdout.write(f"  ✅ Created/Updated: {faq['question']}")

        self.stdout.write(self.style.SUCCESS('✅ E-commerce FAQs seeded successfully!'))