from site_settings.models import SiteSetting 
from categories.models import Category
from pages.models import Page

def global_settings(request):

    setting = SiteSetting.get_instance() 


    footer_categories = Category.objects.filter(
        parent__isnull=True, 
        status=True
    ).prefetch_related('children').order_by('order_level')[:4]
    

    footer_pages = Page.objects.filter(status=True).order_by('order_level')[:4]
    
    return {
        'site_settings': setting,    
        'global_categories': footer_categories,
        'global_pages': footer_pages,
    }