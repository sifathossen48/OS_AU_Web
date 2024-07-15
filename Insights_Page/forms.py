
from django import forms


class InsightSearchForm(forms.Form):
    searchQuery = forms.CharField(max_length=100)