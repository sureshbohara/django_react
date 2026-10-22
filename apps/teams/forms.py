from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name','email', 'address', 'phone', 'bio', 'image', 
            'facebook', 'youtube', 'tiktok', 'instagram', 'order_level', 'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g., john@example.com'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Kathmandu, Nepal'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +977-98XXXXXXXX'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Brief biography, designation...'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'imageInput', 'accept': 'image/png, image/jpeg, image/webp'}), 
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://facebook.com/username'}),
            'youtube': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/@username'}),
            'tiktok': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://tiktok.com/@username'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://instagram.com/username'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0 = Highest priority'}),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[(True, '✅ Active'), (False, '❌ Inactive')]),
        }