from django import forms
from .models import Coupon

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = [
            'code', 'description', 'discount_type', 'discount_value',
            'min_order_amount', 'max_discount', 'usage_limit', 'used_count',
            'usage_limit_per_user', 'start_date', 'end_date', 'status'
        ]
        widgets = {
            'code': forms.TextInput(attrs={
                'class': 'form-control text-uppercase',
                'placeholder': 'e.g., SUMMER20, WELCOME10',
                'style': 'font-weight: 600; letter-spacing: 1px;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief description of the coupon...'
            }),
            'discount_type': forms.Select(attrs={'class': 'form-select'}),
            'discount_value': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'e.g., 10.00'
            }),
            'min_order_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Optional'
            }),
            'max_discount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'For percentage discounts'
            }),
            'usage_limit': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Leave empty for unlimited'
            }),
            'used_count': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'readonly': 'readonly',
                'style': 'background-color: #e9ecef;' 
            }),
            'usage_limit_per_user': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': '1'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
    
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['discount_type'].empty_label = "Select Discount Type"