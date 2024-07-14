from django.contrib import admin

from Insights_Page.models import FutureWork, Insights, InsightsCategory

# Register your models here.
admin.site.register(InsightsCategory)
admin.site.register(Insights)
admin.site.register(FutureWork)