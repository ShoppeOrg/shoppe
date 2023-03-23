from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter
from .models import Product
from .models import ProductInventory
from .models import Review
from .serializers import ProductCreateSerializer
from .serializers import ProductDetailSerializer
from .serializers import ProductInventorySerializer
from .serializers import ProductListSerializer
from .serializers import ReviewListSerializer
from .serializers import ReviewPublishSerializer
from .serializers import ReviewSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related("inventory")
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return ProductCreateSerializer
        if self.action == "list":
            return ProductListSerializer
        if self.action in ("retrieve", "delete"):
            return ProductDetailSerializer

    def get_permissions(self):
        if self.action not in ("list", "retrieve"):
            return [IsAdminUser()]
        return super().get_permissions()


class ProductInventoryRetrieveUpdateAPIVIew(RetrieveUpdateAPIView):
    queryset = ProductInventory.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ProductInventorySerializer


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsAdminUser(),)
        return (IsAuthenticated(),)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewListSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewPublishAPIView(CreateAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ReviewPublishSerializer
