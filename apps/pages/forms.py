from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            'title', 'menu_title', 'slug', 'icon', 'image', 'short_content', 'content',
            'meta_title', 'meta_description', 'meta_keywords',
            'show_in_menu', 'show_in_footer', 'is_featured',
            'order_level', 'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., About Our Company'}),
            'menu_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., About Us (Leave blank to use Title)'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'auto-generated-if-empty'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., bi bi-info-circle'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'imageInput', 'accept': 'image/*'}),
            'short_content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief summary of the page...'}),

            'content': forms.Textarea(attrs={'class': 'form-control summernote', 'rows': 10, 'placeholder': 'Write the main page content here...'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO Title (max 60 chars)'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'SEO Description (max 160 chars)'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comma separated keywords'}),
            'show_in_menu': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'show_in_footer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0 = Highest priority'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }