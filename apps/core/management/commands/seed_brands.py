from django.core.management.base import BaseCommand
from brands.models import Brand

class Command(BaseCommand):
    help = 'Seeds E-commerce Luxury Brands (Minimum 10)'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Luxury Brands...')

        brands_data = [
            {'name': 'Chanel', 'slug': 'chanel', 'description': 'Timeless elegance and luxury fragrances.', 'website': 'https://www.chanel.com', 'order_level': 1},
            {'name': 'Dior', 'slug': 'dior', 'description': 'Innovative beauty and iconic perfumes.', 'website': 'https://www.dior.com', 'order_level': 2},
            {'name': 'Gucci', 'slug': 'gucci', 'description': 'Bold, eclectic, and luxurious scents.', 'website': 'https://www.gucci.com', 'order_level': 3},
            {'name': 'Yves Saint Laurent', 'slug': 'ysl', 'description': 'Edgy, modern, and sophisticated beauty.', 'website': 'https://www.yslbeauty.com', 'order_level': 4},
            {'name': 'Tom Ford', 'slug': 'tom-ford', 'description': 'Ultra-luxurious, niche fragrances and makeup.', 'website': 'https://www.tomford.com', 'order_level': 5},
            {'name': 'La Mer', 'slug': 'la-mer', 'description': 'Premium, transformative skincare products.', 'website': 'https://www.cremedelamer.com', 'order_level': 6},
            {'name': 'Estée Lauder', 'slug': 'estee-lauder', 'description': 'Prestige skincare, makeup, and fragrance.', 'website': 'https://www.esteelauder.com', 'order_level': 7},
            {'name': 'Lancôme', 'slug': 'lancome', 'description': 'French luxury perfumes and cosmetics house.', 'website': 'https://www.lancome.com', 'order_level': 8},
            {'name': 'Creed', 'slug': 'creed', 'description': 'Historic, ultra-luxury niche fragrance house.', 'website': 'https://www.creedfragrances.com', 'order_level': 9},
            {'name': 'Jo Malone London', 'slug': 'jo-malone-london', 'description': 'Exquisite fragrances, bath, and body products.', 'website': 'https://www.jomalone.com', 'order_level': 10},
        ]

        for brand_data in brands_data:
            Brand.objects.update_or_create(
                slug=brand_data['slug'],
                defaults=brand_data
            )
            self.stdout.write(f"  ✅ Created/Updated: {brand_data['name']}")

        self.stdout.write(self.style.SUCCESS('✅ 10 Luxury Brands seeded successfully!'))