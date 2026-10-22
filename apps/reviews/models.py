from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ReviewManager(models.Manager):
    def active(self):
        return self.filter(status=True)

    def ordered(self):
        return self.order_by('order_level', '-created_at')

    def for_page(self, display_on='default'):
        return self.active().filter(display_on=display_on).ordered()


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField(help_text="Main review text")
    content = models.TextField(blank=True, null=True, help_text="Additional content (optional)")
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    display_on = models.CharField(max_length=100, default='default')
    order_level = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewManager()

    class Meta:
        ordering = ['order_level', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/admin/images/noimage.png'

    @property
    def star_rating(self):
        rating = min(max(self.rating, 1), 5)
        return '★' * rating + '☆' * (5 - rating)

    @property
    def has_image(self):
        return bool(self.image)