from unicodedata import category
import django_filters
from django import forms
from .models import Attraction, Category

class AttractionFilterSet(django_filters.FilterSet):

    category = django_filters.filters.ModelChoiceFilter(
        queryset=Category.objects.all(), 
        widget=forms.RadioSelect(attrs={'class':'btn-check'})
        )
    work_in_summer = django_filters.filters.BooleanFilter(widget=forms.CheckboxInput)
    work_in_winter = django_filters.filters.BooleanFilter(widget=forms.CheckboxInput)

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data, queryset, request=request, prefix=prefix)
        self.form.initial['work_in_summer'] =True
        self.form.initial['work_in_winter'] =True

    class Meta:
        model = Attraction
        fields = ['category', 'work_in_summer', 'work_in_winter']