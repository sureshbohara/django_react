from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('dashboard/', include('core.urls')),
    path('products/', include('products.urls')),
    path('categories/', include('categories.urls')),
    path('brands/', include('brands.urls')),
    path('pages/', include('pages.urls')),
    path('blogs/', include('blogs.urls')),
    path('banners/', include('banners.urls')),
    path('faqs/', include('faqs.urls')),
    path('reviews/', include('reviews.urls')),
    path('galleries/', include('galleries.urls')),
    path('teams/', include('teams.urls')),
    path('services/', include('services.urls')),
    path('settings/', include('site_settings.urls')),
    path('login-activities/', include('login_activities.urls')),  
    path('coupons/', include('coupons.urls')),
    path('customers/', include('customers.urls')),
    path('orders/', include('orders.urls')),


    path('', include('frontend.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)