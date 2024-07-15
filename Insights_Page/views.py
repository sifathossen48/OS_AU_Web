from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View

from Insights_Page.models import FutureWork, Insights, InsightsCategory
# from django.db.models import Q
# from django.urls import reverse
from django.contrib import messages

from Insights_Page import forms
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

# def insights_list_search(request):
#     insights= Insights.objects.all()
#     future_works = FutureWork.objects.last() 
    
#     search_item = request.GET.get('q')
    
#     category_items = InsightsCategory.objects.filter(name__contains=search_item)
#     print(category_items)
    
#     return render ( request, 'insights.html', context={'category_items':category_items, 'insights': insights,'future_works':future_works})

def search_news(request):
    insights = Insights.objects.all()
    future_works = FutureWork.objects.last()
    if request.method == 'GET':
        form = forms.InsightSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['searchQuery']
            search_results = Insights.objects.filter(title__contains=query)
            return render(request, 'insights.html', {'results': search_results,
                                                     'query': query,
                                                     'insights': insights,
                                                     'future_works': future_works  
                                                          })
        else:
            messages.error(request, "Invalid data!")
    else:
        form = forms.InsightSearchForm()
    return render(request, 'insights.html', {'form':form})