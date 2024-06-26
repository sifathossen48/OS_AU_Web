from django.contrib import admin

from Home_Page.models import Image, Service, Title

# Register your models here.
admin.site.register(Title)
admin.site.register(Image)
admin.site.register(Service)