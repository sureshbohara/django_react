from django import forms
from .models import SiteSetting

class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        exclude = ['process_item', 'work_item', 'counter_item']
        
        widgets = {
            # --- General ---
            'system_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., My Awesome Company'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'admin@example.com'
            }),
            'extra_email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'support@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '+977-98XXXXXXXX'
            }),
            'extra_phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '+977-01-XXXXXXX'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2, 
                'placeholder': 'Kathmandu, Nepal'
            }),
            'opening_hr': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Sun - Fri, 10:00 AM - 6:00 PM'
            }),
            'work_hours': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., 40 hours/week'
            }),
            'google_map': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': '<iframe src="https://maps.google.com/..."></iframe>'
            }),
            'footer_copyright': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '© 2024 Your Company. All rights reserved.'
            }),
            
            # --- Social ---
            'facebook': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://facebook.com/yourpage'
            }),
            'twitter': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://twitter.com/yourhandle'
            }),
            'linkedin': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://linkedin.com/company/yourcompany'
            }),
            'instagram': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://instagram.com/yourhandle'
            }),
            'youtube': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://youtube.com/@yourchannel'
            }),
            'google': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://yourbusiness.google.com'
            }),
            'yelp': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://yelp.com/biz/yourbusiness'
            }),
            
            # --- Media ---
            'logo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'favicon': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'loader': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'footer_gateway_img': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'bg_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'breadcrumb': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'image1': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'image2': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            
            # --- SEO ---
            'meta_author': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Company Name'
            }),
            'meta_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Best Services in Nepal | Your Company'
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'service, nepal, company, best (comma separated)'
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'We provide the best services in Nepal. Contact us today for a free consultation...'
            }),
            
            # --- Info Blocks ---
            'info1': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'About Us Title'
            }),
            'info2': forms.Textarea(attrs={
                'class': 'form-control summernote', 
                'rows': 3, 
                'placeholder': 'Brief about us description...'
            }),
            'info3': forms.Textarea(attrs={
                'class': 'form-control summernote', 
                'rows': 3, 
                'placeholder': 'More detailed information about the company...'
            }),
            'info4': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Footer short description or copyright info...'
            }),
            'info5': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Our Mission statement...'
            }),
            'info6': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Our Vision statement...'
            }),
            'info7': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Our Core Goals...'
            }),
            
            # --- SMTP ---
            'mail_transport': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'smtp'
            }),
            'mail_host': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'smtp.gmail.com'
            }),
            'mail_port': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': '587'
            }),
            'mail_username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'your_email@gmail.com'
            }),
            'mail_password': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': 'your_app_password'
            }),
            'mail_encryption': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'tls or ssl'
            }),
            'mail_from': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'noreply@yourdomain.com'
            }),
            'mail_from_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Company Name'
            }),
            'smtp_check': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
            # --- Recaptcha ---
            'recaptcha_site_key': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '6LcXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            }),
            'recaptcha_secret_key': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '6LcXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            }),
            'is_recaptcha': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
            # --- API (Google) ---
            'google_analytic_id': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'G-XXXXXXXXXX'
            }),
            'google_client_id': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'XXXXXXXXXXXX-XXXXXXXXXXXXXXXX.apps.googleusercontent.com'
            }),
            'google_client_secret': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'GOCSPX-XXXXXXXXXXXXXXXXXXXX'
            }),
            'google_redirect': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://yourdomain.com/auth/google/callback'
            }),
            'is_google': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
            # --- API (Facebook) ---
            'facebook_analytic_id': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '123456789012345'
            }),
            'facebook_client_id': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '123456789012345'
            }),
            'facebook_client_secret': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            }),
            'facebook_redirect': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://yourdomain.com/auth/facebook/callback'
            }),
            'is_facebook': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
            # --- JSON Titles ---
            'process_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., How We Work'
            }),
            'process_sub_title': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2, 
                'placeholder': 'e.g., Our simple and effective process'
            }),
            'work_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Why Choose Us'
            }),
            'work_sub_title': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2, 
                'placeholder': 'e.g., We deliver excellence in every project'
            }),
            'counter_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., Our Achievements'
            }),
            'counter_sub_title': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2, 
                'placeholder': 'e.g., Numbers that speak for themselves'
            }),
        }