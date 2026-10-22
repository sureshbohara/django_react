from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'parent', 'name', 'slug', 'excerpt', 'description', 
            'image', 'font_icon', 'order_level', 'display_on',
            'meta_keywords', 'meta_description', 'status'
        ]
        widgets = {
            'parent': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Trekking, Wildlife Safari'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'auto-generated-if-empty'
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2, 
                'placeholder': 'Brief summary of the category...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Full description...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 
                'id': 'imageInput',
                'accept': 'image/png, image/jpeg, image/webp'
            }),
            'font_icon': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., bi bi-tags, fa fa-hiking'
            }),
            'order_level': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': 0,
                'placeholder': '0 = Highest priority'
            }),
            'display_on': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('default', 'Default'),
                ('header', 'Header'),
                ('footer', 'Footer'),
            ]),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Comma separated keywords'
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3
            }),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[
                (True, '✅ Active'), 
                (False, '❌ Inactive')
            ]),
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        
        if instance:
            exclude_ids = [instance.id]
            children = instance.get_all_descendants()
            exclude_ids.extend([c.id for c in children])
            self.fields['parent'].queryset = Category.objects.exclude(id__in=exclude_ids)
        else:
            self.fields['parent'].queryset = Category.objects.all()
        
        self.fields['parent'].required = False
        self.fields['parent'].empty_label = '-- None (Root Category) --'