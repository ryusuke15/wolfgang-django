from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import(
    home,
)

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^about',home, name="about"),
    url(r'^contact',home, name="contact"),
    url(r'^shop', home, name="shop"),
    url(r'^shop/(?P<pk>\d+)/$',home),
]
