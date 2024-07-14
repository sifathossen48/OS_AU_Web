import django_filters

from Insights_Page.models import Insights

class InsightsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Insights
        fields = ['category']