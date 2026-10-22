from django.core.management.base import BaseCommand
from categories.models import Category 

class Command(BaseCommand):
    help = 'Seeds E-commerce Categories (7 Main Parents + Subcategories)'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding E-commerce Categories...')

        # 1. PERFUMES & FRAGRANCES
        perfumes, _ = Category.objects.update_or_create(
            slug='perfumes-fragrances', 
            defaults={
                'parent': None, 
                'name': 'Perfumes & Fragrances', 
                'excerpt': 'Discover our curated collection of luxury and artisanal fragrances.', 
                'font_icon': 'bi-droplet-fill', 
                'order_level': 1, 
                'status': True
            }
        )
        perfume_subs = [
            {'name': "Men's Perfumes", 'slug': 'mens-perfumes', 'excerpt': 'Bold, woody, and fresh scents for the modern man.', 'order_level': 1},
            {'name': "Women's Perfumes", 'slug': 'womens-perfumes', 'excerpt': 'Elegant floral, fruity, and oriental fragrances.', 'order_level': 2},
            {'name': 'Unisex Perfumes', 'slug': 'unisex-perfumes', 'excerpt': 'Versatile scents that transcend gender boundaries.', 'order_level': 3},
            {'name': 'Body Mist', 'slug': 'body-mist', 'excerpt': 'Light, refreshing sprays for everyday wear.', 'order_level': 4},
        ]
        for sub in perfume_subs:
            Category.objects.update_or_create(slug=sub['slug'], defaults={'parent': perfumes, 'name': sub['name'], 'excerpt': sub['excerpt'], 'order_level': sub['order_level'], 'status': True})

        # 2. SKINCARE
        skincare, _ = Category.objects.update_or_create(
            slug='skincare', 
            defaults={
                'parent': None, 
                'name': 'Skincare', 
                'excerpt': 'Premium skincare solutions for a radiant, healthy complexion.', 
                'font_icon': 'bi-stars', 
                'order_level': 2, 
                'status': True
            }
        )
        skincare_subs = [
            {'name': 'Face Care', 'slug': 'face-care', 'excerpt': 'Cleansers, toners, and moisturizers for your face.', 'order_level': 1},
            {'name': 'Body Care', 'slug': 'body-care', 'excerpt': 'Nourishing lotions and body washes.', 'order_level': 2},
            {'name': 'Sunscreen', 'slug': 'sunscreen', 'excerpt': 'Protect your skin from harmful UV rays.', 'order_level': 3},
            {'name': 'Anti-Aging', 'slug': 'anti-aging', 'excerpt': 'Serums and creams to reduce fine lines and wrinkles.', 'order_level': 4},
        ]
        for sub in skincare_subs:
            Category.objects.update_or_create(slug=sub['slug'], defaults={'parent': skincare, 'name': sub['name'], 'excerpt': sub['excerpt'], 'order_level': sub['order_level'], 'status': True})

        # 3. MAKEUP
        makeup, _ = Category.objects.update_or_create(
            slug='makeup', 
            defaults={
                'parent': None, 
                'name': 'Makeup', 
                'excerpt': 'High-quality cosmetics to enhance your natural beauty.', 
                'font_icon': 'bi-palette', 
                'order_level': 3, 
                'status': True
            }
        )
        makeup_subs = [
            {'name': 'Face Makeup', 'slug': 'face-makeup', 'excerpt': 'Foundations, concealers, and powders.', 'order_level': 1},
            {'name': 'Eye Makeup', 'slug': 'eye-makeup', 'excerpt': 'Mascaras, eyeliners, and eyeshadow palettes.', 'order_level': 2},
            {'name': 'Lip Care', 'slug': 'lip-care', 'excerpt': 'Lipsticks, glosses, and nourishing balms.', 'order_level': 3},
        ]
        for sub in makeup_subs:
            Category.objects.update_or_create(slug=sub['slug'], defaults={'parent': makeup, 'name': sub['name'], 'excerpt': sub['excerpt'], 'order_level': sub['order_level'], 'status': True})

        # 4. HAIR CARE (New)
        hair_care, _ = Category.objects.update_or_create(
            slug='hair-care', 
            defaults={
                'parent': None, 
                'name': 'Hair Care', 
                'excerpt': 'Nourishing shampoos, conditioners, and treatments for healthy hair.', 
                'font_icon': 'bi-scissors', 
                'order_level': 4, 
                'status': True
            }
        )
        hair_subs = [
            {'name': 'Shampoo & Conditioner', 'slug': 'shampoo-conditioner', 'excerpt': 'Daily cleansing and hydration for all hair types.', 'order_level': 1},
            {'name': 'Hair Styling', 'slug': 'hair-styling', 'excerpt': 'Gels, mousses, and sprays for the perfect look.', 'order_level': 2},
            {'name': 'Hair Treatment', 'slug': 'hair-treatment', 'excerpt': 'Deep conditioning masks and repair serums.', 'order_level': 3},
        ]
        for sub in hair_subs:
            Category.objects.update_or_create(slug=sub['slug'], defaults={'parent': hair_care, 'name': sub['name'], 'excerpt': sub['excerpt'], 'order_level': sub['order_level'], 'status': True})

        # 5. BATH & BODY (New)
        bath_body, _ = Category.objects.update_or_create(
            slug='bath-body', 
            defaults={
                'parent': None, 
                'name': 'Bath & Body', 
                'excerpt': 'Luxurious soaps, scrubs, and lotions for total body relaxation.', 
                'font_icon': 'bi-droplet-half', 
                'order_level': 5, 
                'status': True
            }
        )
        bath_subs = [
            {'name': 'Body Wash', 'slug': 'body-wash', 'excerpt': 'Refreshing and hydrating daily cleansers.', 'order_level': 1},
            {'name': 'Body Lotion', 'slug': 'body-lotion', 'excerpt': 'Deeply moisturizing creams for soft skin.', 'order_level': 2},
            {'name': 'Hand & Foot Care', 'slug': 'hand-foot-care', 'excerpt': 'Specialized care for your hardest working parts.', 'order_level': 3},
        ]
        for sub in bath_subs:
            Category.objects.update_or_create(slug=sub['slug'], defaults={'parent': bath_body, 'name': sub['name'], 'excerpt': sub['excerpt'], 'order_level': sub['order_level'], 'status': True})

        # 6. MEN'S GROOMING (New)
        mens_grooming, _ = Category.objects.update_or_create(
            slug='mens-grooming', 
            defaults={
                'parent': None, 
                'name': "Men's Grooming", 
                'excerpt': 'Essential care products tailored specifically for men.', 
                'font_icon': 'bi-person-badge', 
                'order_level': 6, 
                'status': True
            }
        )
        mens_subs = [
            {'name': 'Beard Care', 'slug': 'beard-care', 'excerpt': 'Oils, balms, and washes for a well-groomed beard.', 'order_level': 1},
            {'name': 'Shaving Essentials', 'slug': 'shaving-essentials', 'excerpt': 'Creams, razors, and aftershaves for a smooth shave.', 'order_level': 2},
            {'name': "Men's Skincare", 'slug': 'mens-skincare', 'excerpt': 'Simple, effective routines for healthy male skin.', 'order_level': 3},
        ]
        for sub in mens_subs:
            Category.objects.update_or_create(slug=sub['slug'], defaults={'parent': mens_grooming, 'name': sub['name'], 'excerpt': sub['excerpt'], 'order_level': sub['order_level'], 'status': True})

        # 7. GIFT SETS & BOXES (New)
        gift_sets, _ = Category.objects.update_or_create(
            slug='gift-sets-boxes', 
            defaults={
                'parent': None, 
                'name': 'Gift Sets & Boxes', 
                'excerpt': 'Perfectly curated bundles for every special occasion.', 
                'font_icon': 'bi-gift', 
                'order_level': 7, 
                'status': True
            }
        )
        gift_subs = [
            {'name': 'Perfume Gift Sets', 'slug': 'perfume-gift-sets', 'excerpt': 'Luxurious fragrance collections for him and her.', 'order_level': 1},
            {'name': 'Skincare Kits', 'slug': 'skincare-kits', 'excerpt': 'Complete routines bundled for glowing skin.', 'order_level': 2},
            {'name': 'Holiday Specials', 'slug': 'holiday-specials', 'excerpt': 'Limited edition festive boxes and bundles.', 'order_level': 3},
        ]
        for sub in gift_subs:
            Category.objects.update_or_create(slug=sub['slug'], defaults={'parent': gift_sets, 'name': sub['name'], 'excerpt': sub['excerpt'], 'order_level': sub['order_level'], 'status': True})

        self.stdout.write(self.style.SUCCESS('✅ 7 Main E-commerce Categories + Subcategories seeded successfully!'))