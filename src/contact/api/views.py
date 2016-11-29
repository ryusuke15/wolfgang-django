from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    )
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from contact.models import Contact, Product, Video_link
from .serializers import (
    ContactCreateSerializer,
    Video_linkSerializer,
    ProductSerializer,
    )

class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
    permission_classes = [AllowAny]

class Video_linkListAPIView(ListAPIView):
    queryset = Video_link.objects.all()
    serializer_class = Video_linkSerializer
    permission_classes = [AllowAny]

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
