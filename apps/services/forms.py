from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'title', 'subtitle', 'icon', 'short_content', 'long_content', 'slug',
            'image', 'feature_image', 'process_title', 'process_sub_title',
            'order_level', 'status', 'meta_keywords', 'meta_description'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter service title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subtitle'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., bi bi-plane'}),
            'short_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description...'}),
            'long_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Detailed description...'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'auto-generated-if-empty'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'imageInput', 'accept': 'image/*'}),
            'feature_image': forms.FileInput(attrs={'class': 'form-control', 'id': 'featureImageInput', 'accept': 'image/*'}),
            'process_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., How It Works'}),
            'process_sub_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief description'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0 = highest priority'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comma separated keywords'}),
            'meta_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO description (150-160 chars)'}),
        }