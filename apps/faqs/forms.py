from django import forms
from .models import Faq

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['display_on', 'question', 'answer', 'order_level', 'status']
        widgets = {
            'display_on': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                ('default', 'Default'),
                ('home', 'Home'),
                ('about', 'About'),
                ('contact', 'Contact'),
                ('services', 'Services'),
                ('booking', 'Booking'),
            ]),
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'e.g., How do I book a trekking package?'
            }),
            'answer': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Provide a clear and detailed answer to the question...'
            }),
            'order_level': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': '0 = Highest priority'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                (True, '✅ Active'),
                (False, '❌ Inactive')
            ]),
        }