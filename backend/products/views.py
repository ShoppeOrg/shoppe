from rest_framework.viewsets import  ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Product
from .serializers import ProductSerializer
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action != 'list':
            return [IsAdminUser()]
        return super().get_permissions()