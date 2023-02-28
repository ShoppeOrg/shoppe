from .models import Product, ProductInventory
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, IntegerField


class ProductListSerializer(HyperlinkedModelSerializer):
    quantity = IntegerField(source="inventory.quantity")

    class Meta:
        model = Product
        fields = ["id", "url", "name", "price", "quantity", "in_stock", "description",  "created_at", "updated_at"]


class ProductDetailSerializer(ModelSerializer):
    quantity = IntegerField(source="inventory.quantity", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "quantity", "in_stock", "description", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class ProductInventorySerializer(ModelSerializer):

    class Meta:
        model = ProductInventory
        fields = ["product_id", "quantity", "sold_qty", "created_at", "updated_at"]