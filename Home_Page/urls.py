from django.urls import path

from . import views

urlpatterns = [
    path("",views.HomeView.as_view(), name="home"),
    path('work/', views.WorkView.as_view(), name="work"),
    path('product/', views.ProductView.as_view(), name="product"),
    path('service/', views.ServiceView.as_view(), name="service"),
    path('insights/', views.InsightsView.as_view(), name="insights")
]
