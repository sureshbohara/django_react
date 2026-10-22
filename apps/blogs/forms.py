from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category', 'title', 'slug', 'image', 'excerpt', 'description',
            'meta_title', 'meta_keywords', 'meta_description', 
            'is_featured', 'order_level', 'status'
        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'auto-generated-if-empty'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'imageInput', 'accept': 'image/*'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief summary...'}),
            
       
            'description': forms.Textarea(attrs={
                'class': 'form-control summernote', 
                'rows': 8, 
                'placeholder': 'Write the main blog content here...'
            }),
            
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO Title (max 60 chars)'}),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., trekking, nepal, tour (comma separated)'
            }),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'SEO Description...'}),
            
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0'}),
            
        
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select Category"