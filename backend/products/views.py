from django.db.models import ObjectDoesNotExist
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from sklearn.metrics.pairwise import paired_euclidean_distances

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


class MostRelatedAPIView(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product_id = self.request.query_params["id"]
        product = Product.objects.select_related("inventory").get(pk=product_id)
        all_products = Product.objects.select_related("inventory").exclude(
            pk=product_id
        )
        related_products = all_products.exclude(inventory__quantity__lte=0)
        if related_products.count() < 3:
            return all_products[:3]
        most_related_map = {}
        for each_product in all_products:
            most_related_map[each_product.id] = paired_euclidean_distances(
                [[each_product.price, each_product.inventory.sold_qty]],
                [[product.price, product.inventory.sold_qty]],
            )[0]
        most_related = sorted(most_related_map.items(), key=lambda x: x[1])[:3]
        return all_products.filter(id__in=[pk for pk, rate in most_related])

    def list(self, request):
        if request.query_params.get("id") is None:
            return Response(
                {"detail": "Missing required query parameter 'id'"}, status=400
            )
        return super().list(request)
