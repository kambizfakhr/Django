from django.db.models import fields
import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrederFilter(django_filters.FilterSet):
    note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created']