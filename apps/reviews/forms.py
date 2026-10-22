from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'name', 'email', 'address', 'rating', 'review',
            'content', 'image', 'display_on', 'order_level', 'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., John Doe'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., john@example.com'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Kathmandu, Nepal'
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write the main review here...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Additional details (optional)...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'imageInput',
                'accept': 'image/png, image/jpeg, image/webp'
            }),
            'order_level': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': '0 = Highest priority'
            }),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
