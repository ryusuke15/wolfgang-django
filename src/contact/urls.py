from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import(
    home,
)

urlpatterns = [
    url(r'^$', home),
    url(r'^about',home),
    url(r'^contact',home),
    url(r'^shop', home),
    url(r'^(?P<pk>\d+)/$',home),
]
