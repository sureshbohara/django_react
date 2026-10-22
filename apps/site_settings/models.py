from django.db import models

class SiteSetting(models.Model):

    # --- General Info ---
    system_name = models.CharField(max_length=191, blank=True, null=True)
    email = models.EmailField(max_length=191, blank=True, null=True)
    extra_email = models.EmailField(max_length=191, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    extra_phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    opening_hr = models.CharField(max_length=100, blank=True, null=True)
    work_hours = models.CharField(max_length=100, blank=True, null=True)
    google_map = models.TextField(blank=True, null=True)
    footer_copyright = models.CharField(max_length=191, blank=True, null=True)
    
    # --- Social ---
    facebook = models.URLField(max_length=191, blank=True, null=True)
    twitter = models.URLField(max_length=191, blank=True, null=True)
    linkedin = models.URLField(max_length=191, blank=True, null=True)
    instagram = models.URLField(max_length=191, blank=True, null=True)
    youtube = models.URLField(max_length=191, blank=True, null=True)
    google = models.URLField(max_length=191, blank=True, null=True)
    yelp = models.URLField(max_length=191, blank=True, null=True)
    
    # --- Media (Images) ---
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    favicon = models.ImageField(upload_to='settings/', blank=True, null=True)
    loader = models.ImageField(upload_to='settings/', blank=True, null=True)
    footer_gateway_img = models.ImageField(upload_to='settings/', blank=True, null=True)
    bg_image = models.ImageField(upload_to='settings/', blank=True, null=True)
    breadcrumb = models.ImageField(upload_to='settings/', blank=True, null=True)
    image1 = models.ImageField(upload_to='settings/', blank=True, null=True)
    image2 = models.ImageField(upload_to='settings/', blank=True, null=True)
    
    # --- SEO ---
    meta_author = models.CharField(max_length=191, blank=True, null=True)
    meta_title = models.CharField(max_length=191, blank=True, null=True)
    meta_keywords = models.CharField(max_length=191, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    
    # --- Info Blocks ---
    info1 = models.TextField(blank=True, null=True)
    info2 = models.TextField(blank=True, null=True)
    info3 = models.TextField(blank=True, null=True)
    info4 = models.TextField(blank=True, null=True)
    info5 = models.TextField(blank=True, null=True)
    info6 = models.TextField(blank=True, null=True)
    info7 = models.TextField(blank=True, null=True)
    
    # --- SMTP ---
    mail_transport = models.CharField(max_length=50, blank=True, null=True)
    mail_host = models.CharField(max_length=191, blank=True, null=True)
    mail_port = models.IntegerField(blank=True, null=True)
    mail_username = models.CharField(max_length=191, blank=True, null=True)
    mail_password = models.CharField(max_length=191, blank=True, null=True)
    mail_encryption = models.CharField(max_length=10, blank=True, null=True)
    mail_from = models.EmailField(max_length=191, blank=True, null=True)
    mail_from_name = models.CharField(max_length=191, blank=True, null=True)
    smtp_check = models.BooleanField(default=False)
    
    # --- Recaptcha ---
    recaptcha_site_key = models.CharField(max_length=191, blank=True, null=True)
    recaptcha_secret_key = models.CharField(max_length=191, blank=True, null=True)
    is_recaptcha = models.BooleanField(default=False)
    
    # --- API (Google/FB) ---
    google_analytic_id = models.CharField(max_length=50, blank=True, null=True)
    google_client_id = models.CharField(max_length=191, blank=True, null=True)
    google_client_secret = models.CharField(max_length=191, blank=True, null=True)
    google_redirect = models.URLField(max_length=191, blank=True, null=True)
    is_google = models.BooleanField(default=False)
    
    facebook_analytic_id = models.CharField(max_length=50, blank=True, null=True)
    facebook_client_id = models.CharField(max_length=191, blank=True, null=True)
    facebook_client_secret = models.CharField(max_length=191, blank=True, null=True)
    facebook_redirect = models.URLField(max_length=191, blank=True, null=True)
    is_facebook = models.BooleanField(default=False)
    

    # --- JSON Fields (Dynamic Items) ---
    process_title = models.CharField(max_length=191, blank=True, null=True)
    process_sub_title = models.TextField(blank=True, null=True)
    process_item = models.JSONField(blank=True, null=True, default=list)
    

    work_title = models.CharField(max_length=191, blank=True, null=True)
    work_sub_title = models.TextField(blank=True, null=True)
    work_item = models.JSONField(blank=True, null=True, default=list)
    

    counter_title = models.CharField(max_length=191, blank=True, null=True)
    counter_sub_title = models.TextField(blank=True, null=True)
    counter_item = models.JSONField(blank=True, null=True, default=list)

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.system_name or "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    @property
    def logo_url(self):
        return self.logo.url if self.logo and hasattr(self.logo, 'url') else '/static/default/noimage.png'

    @property
    def favicon_url(self):
        return self.favicon.url if self.favicon and hasattr(self.favicon, 'url') else '/static/default/noimage.png'

 
    @property
    def footer_gateway_img_url(self):
        return self.footer_gateway_img.url if self.footer_gateway_img and hasattr(self.footer_gateway_img, 'url') else '/static/default/noimage.png'

    @property
    def bg_image_url(self):
        return self.bg_image.url if self.bg_image and hasattr(self.bg_image, 'url') else '/static/default/noimage.png'

    @property
    def breadcrumb_url(self):
        return self.breadcrumb.url if self.breadcrumb and hasattr(self.breadcrumb, 'url') else '/static/default/noimage.png'

    @property
    def image1_url(self):
        return self.image1.url if self.image1 and hasattr(self.image1, 'url') else '/static/default/noimage.png'

    @property
    def image2_url(self):
        return self.image2.url if self.image2 and hasattr(self.image2, 'url') else '/static/default/noimage.png'