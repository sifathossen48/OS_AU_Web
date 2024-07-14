from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from Insights_Page.forms import InsightsFilter
from Insights_Page.models import FutureWork, Insights, InsightsCategory
from django.db.models import Q
from django.urls import reverse
# Create your views here.
class InsightsView(TemplateView):
    template_name = "insights.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insights']= Insights.objects.all()
        context['future_works']= FutureWork.objects.last() 
        return context


class InsightsDetailView(View):
    def get(self, request, insight_id):
        insight = Insights.objects.get(id=insight_id)
        context = {
            'insight': insight,
            'insights': Insights.objects.all(),   
        }
        return render(request, 'single-insights.html', context=context)

def insights_list_search(request):
    insights= Insights.objects.all()
    future_works = FutureWork.objects.last() 
    
    search_item = request.GET.get('q')
    
    category_items = InsightsCategory.objects.filter(name__contains=search_item)
    print(category_items)
    
    return render ( request, 'insights.html', context={'category_items':category_items, 'insights': insights,'future_works':future_works})