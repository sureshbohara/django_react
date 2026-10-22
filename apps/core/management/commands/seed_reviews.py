from django.core.management.base import BaseCommand
from reviews.models import Review 

class Command(BaseCommand):
    help = 'Seeds E-commerce Customer Reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Customer Reviews...')

        reviews_data = [
            {
                'name': 'Sophia L.',
                'email': 'sophia.l@example.com',
                'address': 'Kathmandu, Nepal',
                'rating': 5,
                'review': 'Absolutely love the Rose Elixir! The scent is romantic and lasts all day. The packaging is also incredibly luxurious.',
                'content': 'Fast delivery and excellent customer service. Will definitely be ordering again.',
                'display_on': 'home',
                'order_level': 1,
                'status': True,
            },
            {
                'name': 'James H.',
                'email': 'james.h@example.com',
                'address': 'Pokhara, Nepal',
                'rating': 5,
                'review': 'The Midnight Oud perfume is very masculine and sophisticated. Gets me so many compliments!',
                'content': 'Great quality for the price. Highly recommend for anyone looking for a niche fragrance.',
                'display_on': 'home',
                'order_level': 2,
                'status': True,
            },
            {
                'name': 'Olivia M.',
                'email': 'olivia.m@example.com',
                'address': 'Lalitpur, Nepal',
                'rating': 4,
                'review': 'The Vitamin C Serum is amazing. I\'ve noticed a visible difference in my skin brightness after just two weeks.',
                'content': 'The only reason for 4 stars is that the bottle is a bit small, but the quality is top-notch.',
                'display_on': 'home',
                'order_level': 3,
                'status': True,
            },
            {
                'name': 'David Miller',
                'email': 'david.m@example.com',
                'address': 'Bhaktapur, Nepal',
                'rating': 5,
                'review': 'Bought the Velvet Matte Lipstick set for my wife. She absolutely loves the shades and the formula is very hydrating.',
                'content': 'Beautiful gift packaging. Thank you for making our anniversary special!',
                'display_on': 'home',
                'order_level': 4,
                'status': True,
            },
        ]

        for review in reviews_data:
            Review.objects.update_or_create(
                email=review['email'],
                defaults=review
            )

        self.stdout.write(self.style.SUCCESS('✅ Reviews seeded successfully!'))