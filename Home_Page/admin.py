from django.contrib import admin

from Home_Page.models import Company_Achievement, Image, Product, Service, Technology, Title

# Register your models here.
admin.site.register(Title)
admin.site.register(Image)
admin.site.register(Service)
admin.site.register(Company_Achievement)
admin.site.register(Technology)
admin.site.register(Product)