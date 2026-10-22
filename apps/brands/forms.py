from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            'name', 'slug', 'logo', 'description', 'website', 
            'meta_title', 'meta_keywords', 'meta_description', 
            'order_level', 'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Nike, Adidas, Apple'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'auto-generated-if-empty'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imageInput', 
                'accept': 'image/png, image/jpeg, image/webp'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Brief description of the brand and its history...'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://example.com'
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'SEO Title (e.g., Nike Official Store)'
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., shoes, sportswear, nike (comma separated)'
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'SEO Description (max 160 characters)...'
            }),
            'order_level': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': 0, 
                'placeholder': '0 = Highest priority'
            }),

            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }