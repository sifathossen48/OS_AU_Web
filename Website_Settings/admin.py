from django.contrib import admin

from Website_Settings.models import Background, Setting

# Register your models here.
admin.site.register(Setting)
admin.site.register(Background)