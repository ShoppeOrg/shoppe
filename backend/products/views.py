from django.db.models import ObjectDoesNotExist
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView
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
    filterset_class = ProductFilter

    def get_queryset(self):
        if self.action == "retrieve":
            return Product.objects.select_related(
                "inventory", "main_image"
            ).prefetch_related("reviews", "reviews__user", "images")
        return Product.objects.select_related("inventory", "main_image")

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return ProductCreateSerializer
        if self.action in ("retrieve", "delete"):
            return ProductDetailSerializer
        return ProductListSerializer

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


class ReviewPublishAPIView(APIView):
    queryset = Review.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ReviewPublishSerializer

    def post(self, request, pk=None):
        try:
            product_review = Review.objects.get(pk=pk)
            product_review.is_published = True
            product_review.save()
        except ObjectDoesNotExist:
            return Response(
                {"detail": {"info": "Review with given id was not found", "pk": pk}},
                status=HTTP_404_NOT_FOUND,
            )
        return Response({"detail": "Review has been published."}, status=200)
