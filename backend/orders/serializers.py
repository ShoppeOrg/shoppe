from products.models import ProductInventory
from rest_framework.serializers import IntegerField
from rest_framework.serializers import ModelSerializer


class CheckProductsAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ["product", "quantity"]
