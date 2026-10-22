from django import forms
from .models import Product, ProductAttribute, ProductVariant

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'slug', 'sku', 'barcode', 'product_type',
            'regular_price', 'sale_price', 'sale_price_start', 'sale_price_end',
            'manage_stock', 'stock_quantity', 'stock_status', 'low_stock_threshold',
            'short_description', 'description',
            'thumbnail', 'video_url', 'downloadable_file', 'download_limit', 'download_expiry_days',
            'is_featured', 'is_virtual', 'order_level', 'status',
            'meta_title', 'meta_description','meta_keywords', 'brand', 'category'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Classic T-Shirt'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'auto-generated-if-empty'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., TSH-001'}),
            'barcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 123456789'}),
            'product_type': forms.Select(attrs={'class': 'form-select'}),
            'regular_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'sale_price_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sale_price_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'manage_stock': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0'}),
            'stock_status': forms.Select(attrs={'class': 'form-select'}),
            'low_stock_threshold': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '5'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief summary of the product...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Detailed product description...'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control', 'id': 'thumbInput', 'accept': 'image/*'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://youtube.com/...'}),
            'downloadable_file': forms.FileInput(attrs={'class': 'form-control'}),
            'download_limit': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'e.g., 3'}),
            'download_expiry_days': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'e.g., 30'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_virtual': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO Title'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO keywords'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'SEO Description...'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].empty_label = "Select Brand"
        self.fields['category'].empty_label = "Select Category"
        self.fields['product_type'].empty_label = "Select Product Type"
        self.fields['stock_status'].empty_label = "Select Stock Status"


class ProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        fields = ['name', 'slug', 'type', 'order_level', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Size, Color'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'auto-generated'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'order_level': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Select Type"


class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['sku', 'price', 'sale_price', 'stock_quantity', 'attributes', 'image', 'status']
        widgets = {
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., VAR-001'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': '0'}),
            'attributes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'JSON: {"Size": "L", "Color": "Red"}'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }