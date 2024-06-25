from django.contrib import admin

from About_Page.models import Core_Values, Page_Settings

# Register your models here.
admin.site.register(Page_Settings)
admin.site.register(Core_Values)