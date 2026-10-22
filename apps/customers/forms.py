from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'info', 'image', 'is_active', 'subscribed_to_newsletter']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g., john@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+977-98XXXXXXXX'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Full address...'}),
            'info': forms.Textarea(attrs={'class': 'form-control summernote', 'rows': 3, 'placeholder': 'Additional notes...'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'imageInput', 'accept': 'image/*'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'subscribed_to_newsletter': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CustomerEmailForm(forms.Form):
    RECIPIENT_CHOICES = [
        ('all', 'All Active Customers'),
        ('subscribed', 'Only Newsletter Subscribers'),
    ]
    
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'e.g., Dashain Special 50% Off!'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control summernote', 'rows': 6, 'placeholder': 'Write your email content here...'
    }))
    recipient_type = forms.ChoiceField(choices=RECIPIENT_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))