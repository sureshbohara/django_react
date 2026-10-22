from django.core.management.base import BaseCommand
from products.models import ProductAttribute

class Command(BaseCommand):
    help = 'Seeds E-commerce Product Attributes (Size, Color, Skin Type, etc.)'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding Product Attributes...')

        attributes_data = [
            {
                'name': 'Size',
                'slug': 'size',
                'type': 'select',
                'values': ['50ml', '100ml', '200ml', '500ml', '1 Litre'],
                'order_level': 1,
                'status': True,
            },
            {
                'name': 'Volume',
                'slug': 'volume',
                'type': 'select',
                'values': ['15ml', '30ml', '50ml', '100ml', '150ml'],
                'order_level': 2,
                'status': True,
            },
            {
                'name': 'Skin Type',
                'slug': 'skin-type',
                'type': 'select',
                'values': ['Oily', 'Dry', 'Combination', 'Sensitive', 'Normal', 'All Skin Types'],
                'order_level': 3,
                'status': True,
            },
            {
                'name': 'Fragrance Family',
                'slug': 'fragrance-family',
                'type': 'select',
                'values': ['Floral', 'Woody', 'Citrus', 'Oriental', 'Fresh', 'Fruity', 'Gourmand'],
                'order_level': 4,
                'status': True,
            },
            {
                'name': 'Gender',
                'slug': 'gender',
                'type': 'select',
                'values': ['Men', 'Women', 'Unisex', 'Kids'],
                'order_level': 5,
                'status': True,
            },
            {
                'name': 'Color',
                'slug': 'color',
                'type': 'color',
                'values': ['Red', 'Pink', 'Nude', 'Berry', 'Coral', 'Brown', 'Black'],
                'order_level': 6,
                'status': True,
            },
            {
                'name': 'Hair Type',
                'slug': 'hair-type',
                'type': 'select',
                'values': ['Straight', 'Wavy', 'Curly', 'Coily', 'Damaged', 'Color-Treated'],
                'order_level': 7,
                'status': True,
            },
            {
                'name': 'Concern',
                'slug': 'concern',
                'type': 'select',
                'values': ['Anti-Aging', 'Acne', 'Hyperpigmentation', 'Dryness', 'Dullness', 'Wrinkles'],
                'order_level': 8,
                'status': True,
            },
        ]

        for attr_data in attributes_data:
            ProductAttribute.objects.update_or_create(
                slug=attr_data['slug'],
                defaults=attr_data
            )
            self.stdout.write(f"  ✅ Created/Updated: {attr_data['name']} ({len(attr_data['values'])} values)")

        self.stdout.write(self.style.SUCCESS('✅ Product Attributes seeded successfully!'))