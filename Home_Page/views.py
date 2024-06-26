from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from Home_Page.models import Image, Service, Title
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titles'] = Title.objects.all()
        context['img'] = Image.objects.last()
        context['services'] = Service.objects.all()
        return context
class WorkView(TemplateView):
    template_name = "work.html"
class ProductView(TemplateView):
    template_name = "products.html"
class ServiceView(TemplateView):
    template_name = "services.html"

class ServiceDetailView(View):
    def get(self, request, service_id):
        service = Service.objects.get(id=service_id)
        context = {
            'service': service,
            'services': Service.objects.all(),
        }
        return render(request, 'service-details.html', context=context)
    
class InsightsView(TemplateView):
    template_name = "insights.html"
class CareerView(TemplateView):
    template_name = "careers.html"