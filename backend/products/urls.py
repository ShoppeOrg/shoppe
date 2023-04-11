from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductInventoryRetrieveUpdateAPIVIew
from .views import ProductViewSet
from .views import ReviewListCreateAPIView

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
urlpatterns = [
    path("products/reviews/", ReviewListCreateAPIView.as_view(), name="product_review"),
    path(
        "products/<int:pk>/inventory/",
        ProductInventoryRetrieveUpdateAPIVIew.as_view(),
        name="product_inventory",
    ),
]
urlpatterns += router.urls
