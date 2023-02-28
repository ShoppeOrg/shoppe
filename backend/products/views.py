from rest_framework.viewsets import  ModelViewSet
from rest_framework.permissions import IsAdminUser
from .filters import ProductFilter
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.select_related('inventory')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.action not in ('list', 'detail'):
            return [IsAdminUser()]
        return super().get_permissions()
