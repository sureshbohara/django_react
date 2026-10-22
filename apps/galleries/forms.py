from django import forms
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'alt', 'image', 'display_on', 'order_level', 'status']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Everest Base Camp Trek'
            }),
            'alt': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the image for SEO and accessibility'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'imageInput',
                'accept': 'image/png, image/jpeg, image/webp'
            }),
            'display_on': forms.Select(attrs={
                'class': 'form-select'
            }, choices=[
                ('default', 'Default'),
                ('home', 'Home Page'),
                ('gallery_page', 'Gallery Page'),
                ('about', 'About Page'),
            ]),
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