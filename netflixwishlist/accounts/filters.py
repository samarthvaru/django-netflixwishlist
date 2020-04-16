import django_filters
from django_filters import CharFilter
from .models import *


class ListFilter(django_filters.FilterSet):
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model=ListItem
        fields='__all__'
        exclude=['customer']