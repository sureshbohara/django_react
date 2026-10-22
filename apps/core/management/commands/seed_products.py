from django.core.management.base import BaseCommand
from products.models import Product
from categories.models import Category
from brands.models import Brand

class Command(BaseCommand):
    help = 'Seeds E-commerce Products perfectly matched for Homepage sections'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding E-commerce Products...')

        # Safe fetching helper functions
        def get_cat(slug):
            return Category.objects.filter(slug=slug).first()

        def get_brand(slug):
            return Brand.objects.filter(slug=slug).first()

        mens_perfume = get_cat('mens-perfumes')
        womens_perfume = get_cat('womens-perfumes')
        face_care = get_cat('face-care')
        lip_care = get_cat('lip-care')
        body_mist = get_cat('body-mist')
        hair_care = get_cat('hair-care')

        chanel = get_brand('chanel')
        dior = get_brand('dior')
        la_mer = get_brand('la-mer')
        ysl = get_brand('ysl')
        tom_ford = get_brand('tom-ford')

        products_data = [
          
            {
                'name': 'Midnight Oud - Luxury Men\'s Perfume (100ml)',
                'slug': 'midnight-oud-luxury-mens-perfume',
                'sku': 'PRD-001', 'brand': chanel, 'category': mens_perfume,
                'regular_price': 5200.00, 'sale_price': 4500.00, 
                'short_description': 'A bold, woody, and mysterious fragrance for the modern man.',
                'description': '<p>Midnight Oud is a captivating blend of rich oud wood, spicy saffron, and warm amber.</p>',
                'manage_stock': True, 'stock_quantity': 50, 'is_featured': True, 'status': True, 'order_level': 1,
            },
            {
                'name': 'Rose Elixir Eau de Parfum (50ml)',
                'slug': 'rose-elixir-eau-de-parfum',
                'sku': 'PRD-002', 'brand': dior, 'category': womens_perfume,
                'regular_price': 5500.00, 'sale_price': 3200.00, 
                'short_description': 'A romantic and intoxicating blend of Bulgarian rose and vanilla.',
                'description': '<p>Experience the essence of a thousand roses. Elegant and sophisticated.</p>',
                'manage_stock': True, 'stock_quantity': 30, 'is_featured': True, 'status': True, 'order_level': 2,
            },
            {
                'name': 'Glow Boost Vitamin C Face Serum (30ml)',
                'slug': 'glow-boost-vitamin-c-face-serum',
                'sku': 'PRD-003', 'brand': la_mer, 'category': face_care,
                'regular_price': 1800.00, 'sale_price': 1250.00, 
                'short_description': 'Brighten your complexion with this powerful Vitamin C serum.',
                'description': '<p>Formulated with 15% pure Vitamin C to visibly brighten skin and reduce dark spots.</p>',
                'manage_stock': True, 'stock_quantity': 100, 'is_featured': True, 'status': True, 'order_level': 3,
            },
            {
                'name': 'Velvet Matte Lipstick Collection (Set of 3)',
                'slug': 'velvet-matte-lipstick-collection',
                'sku': 'PRD-004', 'brand': ysl, 'category': lip_care,
                'regular_price': 2100.00, 'sale_price': 1500.00, 
                'short_description': 'Three stunning shades of long-lasting, hydrating matte lipstick.',
                'description': '<p>Includes Classic Red, Nude Beige, and Berry Plum. Enriched with Vitamin E.</p>',
                'manage_stock': True, 'stock_quantity': 75, 'is_featured': True, 'status': True, 'order_level': 4,
            },

          
            {
                'name': 'Hydrating Night Cream (50ml)',
                'slug': 'hydrating-night-cream',
                'sku': 'PRD-005', 'brand': la_mer, 'category': face_care,
                'regular_price': 4000.00, 'sale_price': None, 
                'short_description': 'Wake up to plump, radiant, and deeply nourished skin.',
                'description': '<p>This rich night cream works while you sleep to repair the skin barrier.</p>',
                'manage_stock': True, 'stock_quantity': 40, 'is_featured': True, 'status': True, 'order_level': 5,
            },
            {
                'name': 'Lavender Sleep Mist (100ml)',
                'slug': 'lavender-sleep-mist',
                'sku': 'PRD-006', 'brand': None, 'category': body_mist,
                'regular_price': 1200.00, 'sale_price': None,
                'short_description': 'Calming pillow and room spray for a restful night\'s sleep.',
                'description': '<p>Infused with pure lavender essential oil and chamomile extract.</p>',
                'manage_stock': True, 'stock_quantity': 60, 'is_featured': True, 'status': True, 'order_level': 6,
            },
            {
                'name': 'Sandalwood & Leather Cologne',
                'slug': 'sandalwood-leather-cologne',
                'sku': 'PRD-007', 'brand': tom_ford, 'category': mens_perfume,
                'regular_price': 6500.00, 'sale_price': None,
                'short_description': 'A sophisticated, masculine scent with deep woody notes.',
                'description': '<p>Premium cologne featuring notes of sandalwood, leather, and black pepper.</p>',
                'manage_stock': True, 'stock_quantity': 25, 'is_featured': True, 'status': True, 'order_level': 7,
            },
            {
                'name': 'Citrus & Sea Salt Body Wash',
                'slug': 'citrus-sea-salt-body-wash',
                'sku': 'PRD-008', 'brand': None, 'category': body_mist,
                'regular_price': 950.00, 'sale_price': None,
                'short_description': 'Refreshing daily body wash with a crisp, oceanic scent.',
                'description': '<p>Sulfate-free formula that cleanses without stripping natural oils.</p>',
                'manage_stock': True, 'stock_quantity': 120, 'is_featured': True, 'status': True, 'order_level': 8,
            },

            {
                'name': 'Pure Argan Oil Repair Shampoo (500ml)',
                'slug': 'pure-argan-oil-repair-shampoo',
                'sku': 'PRD-009', 'brand': None, 'category': hair_care,
                'regular_price': 1100.00, 'sale_price': None,
                'short_description': 'Restore shine and strength to damaged hair with pure Argan oil.',
                'description': '<p>Deeply nourishing shampoo infused with Moroccan Argan oil and Keratin.</p>',
                'manage_stock': True, 'stock_quantity': 80, 'is_featured': False, 'status': True, 'order_level': 9,
            },
            {
                'name': 'Gold Radiance Face Oil',
                'slug': 'gold-radiance-face-oil',
                'sku': 'PRD-010', 'brand': la_mer, 'category': face_care,
                'regular_price': 5000.00, 'sale_price': None,
                'short_description': 'Luxurious facial oil for a glowing, youthful complexion.',
                'description': '<p>Blended with 24k gold particles and rosehip oil for ultimate radiance.</p>',
                'manage_stock': True, 'stock_quantity': 15, 'is_featured': False, 'status': True, 'order_level': 10,
            },
            {
                'name': 'Floral Dream Eau de Parfum',
                'slug': 'floral-dream-eau-de-parfum',
                'sku': 'PRD-011', 'brand': chanel, 'category': womens_perfume,
                'regular_price': 4500.00, 'sale_price': None,
                'short_description': 'A light, airy fragrance featuring notes of jasmine and peony.',
                'description': '<p>Perfect for spring and summer days. Fresh, clean, and uplifting.</p>',
                'manage_stock': True, 'stock_quantity': 45, 'is_featured': False, 'status': True, 'order_level': 11,
            },
            {
                'name': 'Daily Health Multivitamin Gummies',
                'slug': 'daily-health-multivitamin-gummies',
                'sku': 'PRD-012', 'brand': None, 'category': face_care,
                'regular_price': 1500.00, 'sale_price': None,
                'short_description': 'Delicious gummies packed with essential vitamins for daily wellness.',
                'description': '<p>Vegan, gluten-free gummies with Vitamin C, D, and B12.</p>',
                'manage_stock': True, 'stock_quantity': 200, 'is_featured': False, 'status': True, 'order_level': 12,
            },
            {
                'name': 'Aromatherapy Essential Oil Diffuser',
                'slug': 'aromatherapy-essential-oil-diffuser',
                'sku': 'PRD-013', 'brand': None, 'category': body_mist,
                'regular_price': 3000.00, 'sale_price': None,
                'short_description': 'Ultrasonic diffuser to create a calming atmosphere in your home.',
                'description': '<p>Features 7 LED light colors and auto-shutoff for safety.</p>',
                'manage_stock': True, 'stock_quantity': 30, 'is_featured': False, 'status': True, 'order_level': 13,
            },
            {
                'name': 'Brightening Niacinamide Serum',
                'slug': 'brightening-niacinamide-serum',
                'sku': 'PRD-014', 'brand': None, 'category': face_care,
                'regular_price': 2200.00, 'sale_price': None,
                'short_description': 'Advanced formula for an even skin tone and radiant glow.',
                'description': '<p>Contains stable Niacinamide and Zinc for maximum efficacy and pore refining.</p>',
                'manage_stock': True, 'stock_quantity': 90, 'is_featured': False, 'status': True, 'order_level': 14,
            },
        ]

        for prod_data in products_data:
            Product.objects.update_or_create(
                slug=prod_data['slug'],
                defaults=prod_data
            )
            self.stdout.write(f"  ✅ Created/Updated: {prod_data['name']}")

        self.stdout.write(self.style.SUCCESS('🚀 14 E-commerce Products seeded successfully!'))