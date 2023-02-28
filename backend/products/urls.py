from django.urls import path
from .views import ProductViewSet, ProductInventoryRetrieveUpdateAPIVIew
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
urlpatterns = [
    path("products/<int:pk>/inventory", ProductInventoryRetrieveUpdateAPIVIew.as_view())
]
urlpatterns += router.urls
