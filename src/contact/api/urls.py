from django.conf.urls import url

from .views import (
    ContactCreateAPIView,
    Video_linkListAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    )

urlpatterns = [
    url(r'^create/$', ContactCreateAPIView.as_view(), name='create'),
    url(r'^video_links/$', Video_linkListAPIView.as_view(), name='list_video'),   
    url(r'^products/$', ProductListAPIView.as_view(), name='list_product'),   
    url(r'^products/(?P<pk>\d+)/$', ProductDetailAPIView.as_view(), name='detail_product'),  
]
