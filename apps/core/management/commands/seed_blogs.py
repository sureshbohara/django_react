from django.core.management.base import BaseCommand
from blogs.models import Post
from categories.models import Category

class Command(BaseCommand):
    help = 'Seeds E-commerce Blog Posts with realistic, SEO-friendly content'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌱 Seeding E-commerce Blog Posts...')

        # Helper to get category safely
        def get_category(slug):
            return Category.objects.filter(slug=slug).first()

        perfume_cat = get_category('perfumes-fragrances')
        skincare_cat = get_category('skincare')
        makeup_cat = get_category('makeup')

        posts_data = [
            {
                'title': 'How to Choose the Perfect Signature Scent',
                'slug': 'how-to-choose-perfect-signature-scent',
                'category': perfume_cat,
                'excerpt': 'Finding your signature fragrance is a deeply personal journey. Here are our top tips for selecting a scent that truly represents you.',
                'description': '<p>Finding your signature fragrance is a deeply personal journey. Your scent is an invisible accessory that leaves a lasting impression.</p><h3>1. Understand Fragrance Families</h3><p>Before you spray, it helps to know the main fragrance families: Floral, Woody, Oriental, and Fresh. Do you prefer the light, airy feel of citrus, or the deep, mysterious notes of oud?</p><h3>2. Test on Your Skin</h3><p>Fragrances react differently to everyone\'s unique skin chemistry. Always test a perfume on your wrist and wait at least 30 minutes to see how the top, middle, and base notes develop.</p><h3>3. Consider the Occasion</h3><p>You might want a light, fresh scent for the office and a bold, spicy fragrance for evening events.</p>',
                'meta_title': 'How to Choose the Perfect Signature Scent | Caroline\'s House',
                'meta_description': 'Discover expert tips on how to find and choose your perfect signature fragrance that matches your personality and style.',
                'meta_keywords': 'signature scent, how to choose perfume, fragrance guide, perfume tips',
                'views': 1250,
                'is_featured': True,
                'status': True,
                'order_level': 1,
            },
            {
                'title': 'The Ultimate Guide to Layering Skincare Products',
                'slug': 'ultimate-guide-layering-skincare-products',
                'category': skincare_cat,
                'excerpt': 'Confused about the right order to apply your serums and moisturizers? Our step-by-step guide will help you maximize your skincare routine.',
                'description': '<p>Applying your skincare products in the correct order is crucial for maximizing their effectiveness. Here is the golden rule: apply products from thinnest to thickest consistency.</p><h3>Step 1: Cleanser</h3><p>Start with a clean canvas. Use a gentle cleanser to remove dirt, oil, and makeup.</p><h3>Step 2: Toner</h3><p>Balance your skin\'s pH and prepare it to absorb the next layers.</p><h3>Step 3: Serums</h3><p>This is where the magic happens. Apply your active ingredients, like Vitamin C in the morning or Retinol at night.</p><h3>Step 4: Moisturizer</h3><p>Lock in all the hydration and active ingredients with a good quality moisturizer.</p><h3>Step 5: Sunscreen (AM only)</h3><p>Never skip this! SPF is your best defense against premature aging.</p>',
                'meta_title': 'The Ultimate Guide to Layering Skincare Products',
                'meta_description': 'Learn the correct order to apply your skincare products to get the best results. A step-by-step guide for glowing skin.',
                'meta_keywords': 'skincare routine, layering skincare, skincare order, beauty guide',
                'views': 890,
                'is_featured': True,
                'status': True,
                'order_level': 2,
            },
            {
                'title': '5 Makeup Trends Dominating This Season',
                'slug': '5-makeup-trends-dominating-this-season',
                'category': makeup_cat,
                'excerpt': 'From glossy lids to bold berry lips, discover the top 5 makeup trends you need to try this season to elevate your look.',
                'description': '<p>Makeup trends are constantly evolving, but this season is all about enhancing your natural beauty with a touch of glamour.</p><ul><li><strong>Glossy Eyelids:</strong> Ditch the heavy eyeshadow for a fresh, dewy lid.</li><li><strong>Bold Berry Lips:</strong> Deep plum and cherry red shades are making a major comeback.</li><li><strong>Flushed Cheeks:</strong> Cream blushes applied high on the cheekbones give a youthful, natural glow.</li><li><strong>Graphic Liner:</strong> Playful, colorful eyeliner is a fun way to express your personality.</li><li><strong>Barely-There Base:</strong> Lightweight tinted moisturizers and concealers are replacing heavy foundations.</li></ul>',
                'meta_title': '5 Makeup Trends Dominating This Season | Beauty Blog',
                'meta_description': 'Explore the top 5 makeup trends of the season, from glossy lids to bold berry lips, and learn how to achieve the look.',
                'meta_keywords': 'makeup trends, beauty trends, seasonal makeup, makeup tips',
                'views': 650,
                'is_featured': False,
                'status': True,
                'order_level': 3,
            },
            {
                'title': 'Why Natural and Organic Beauty Products Are Worth the Investment',
                'slug': 'why-natural-organic-beauty-products-worth-investment',
                'category': skincare_cat,
                'excerpt': 'Discover the benefits of switching to natural and organic beauty products for your skin and the environment.',
                'description': '<p>The beauty industry is shifting towards cleaner, more sustainable ingredients. But are natural and organic products really worth the hype?</p><p><strong>Gentler on the Skin:</strong> Natural products are free from harsh chemicals, synthetic fragrances, and parabens, making them ideal for sensitive skin.</p><p><strong>Rich in Nutrients:</strong> Plant-based ingredients are packed with vitamins, antioxidants, and essential fatty acids that nourish the skin from within.</p><p><strong>Eco-Friendly:</strong> Organic farming practices are better for the environment, and many natural beauty brands use sustainable, recyclable packaging.</p><p>Making the switch might seem daunting, but starting with one or two products, like a natural cleanser or serum, can make a noticeable difference.</p>',
                'meta_title': 'Why Natural and Organic Beauty Products Are Worth It',
                'meta_description': 'Learn why investing in natural and organic beauty products is beneficial for your skin health and the environment.',
                'meta_keywords': 'organic beauty, natural skincare, clean beauty, eco-friendly cosmetics',
                'views': 420,
                'is_featured': False,
                'status': True,
                'order_level': 4,
            },
        ]

        created_count = 0
        for post_data in posts_data:
            Post.objects.update_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            self.stdout.write(f"  ✅ Created/Updated: {post_data['title']}")
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f'🚀 {created_count} Blog Posts seeded successfully!'))