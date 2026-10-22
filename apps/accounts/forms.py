from django import forms
from .models import AdminUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['name', 'email', 'mobile', 'address', 'details', 'gender', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g., john@example.com'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +977 98XXXXXXXX'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Street, City, State'}),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief professional bio...'}),
            'gender': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('', '-- Select Gender --'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')
            ]),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'profileImageInput', 'accept': 'image/*'}),
        }

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter current password'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Minimum 8 characters'}),
        min_length=8
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter new password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')
        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError({"password": "Passwords don't match"})
        return cleaned_data

class AdminUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Leave blank to keep current'}),
        required=False
    )

    class Meta:
        model = AdminUser
        fields = ['name', 'email', 'mobile', 'address', 'gender', 'details', 'image', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g., john@example.com'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +977 98XXXXXXXX'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Street, City, State'}),
            'gender': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('', '-- Select Gender --'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')
            ]),
            'details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief bio...'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'status': forms.Select(attrs={'class': 'form-select'}, choices=[(True, '✅ Active'), (False, '❌ Inactive')]),
        }