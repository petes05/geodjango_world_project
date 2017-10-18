from django.core.serializers import serialize
from django.http import HttpResponse
from django.views import generic

from .models import WorldBorder


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'world/index.html'
    context_object_name = 'countries_list'

    def get_queryset(self):
        return WorldBorder.objects.values_list('name', flat=True).order_by('name')


def country_borders_dataset(request, countryname):
    country_borders = serialize('geojson', WorldBorder.objects.filter(name=countryname))
    return HttpResponse(country_borders, content_type='json')