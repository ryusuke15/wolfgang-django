from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^', include("contact.urls")),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/contacts/', include("contact.api.urls", namespace='contacts-api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
