from django.shortcuts import render
from django.views.generic import TemplateView

from Home_Page.models import Image, Title
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titles'] = Title.objects.all()
        context['img'] = Image.objects.last()
        return context
class WorkView(TemplateView):
    template_name = "work.html"
class ProductView(TemplateView):
    template_name = "products.html"
class ServiceView(TemplateView):
    template_name = "services.html"
class InsightsView(TemplateView):
    template_name = "insights.html"