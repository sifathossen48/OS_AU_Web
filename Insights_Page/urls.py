from django.urls import path

from . import views

urlpatterns = [
    path("",views.InsightsView.as_view(), name="insights"),
    path('details/<int:insight_id>', views.InsightsDetailView.as_view(), name='insights-details'),
    path('search_category/', views.insights_list_search, name="insight-search")
]