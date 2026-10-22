from django import forms
from .models import Banner

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['title', 'subtitle', 'image', 'description', 'order_level', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'required': True,
                'placeholder': 'e.g., Summer Vacation Special Offer'
            }),
            'subtitle': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Get 20% off on all packages'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imageInput',
                'accept': 'image/png, image/jpeg, image/webp'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 6, 
                'placeholder': 'Brief description or call-to-action...'
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