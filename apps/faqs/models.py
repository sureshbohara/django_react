from django.db import models

class Faq(models.Model):
    display_on = models.CharField(max_length=255, default='default')
    question = models.TextField()
    answer = models.TextField()
    order_level = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order_level', '-created_at']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question[:50]