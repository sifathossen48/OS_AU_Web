from django.shortcuts import render
from django.views.generic import TemplateView

from Home_Page.models import Title
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titles'] = Title.objects.all()
        return context