from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from .filters import ProductFilter
from .models import Product, ProductInventory
from .serializers import (
    ProductListSerializer, ProductDetailSerializer, ProductInventorySerializer, ProductCreateSerializer
)


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.select_related('inventory')
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return ProductCreateSerializer
        if self.action == 'list':
            return ProductListSerializer
        if self.action in ('retrieve', 'delete'):
            return ProductDetailSerializer

    def get_permissions(self):
        if self.action not in ('list', 'retrieve'):
            return [IsAdminUser()]
        return super().get_permissions()


class ProductInventoryRetrieveUpdateAPIVIew(RetrieveUpdateAPIView):
    queryset = ProductInventory.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ProductInventorySerializer
