import django_filters
from django_filters import filters
from django_filters.filters import Filter
from .models import Destination



class DestinationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Destination
        fields = '__all__'
        exclude = ['image' ,'price', 'description' ,'created_at']