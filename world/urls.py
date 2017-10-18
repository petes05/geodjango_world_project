from django.conf.urls import url

from . import views

app_name = 'world'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<countryname>.+)/countries/$', views.country_borders_dataset, name='countries'),
]