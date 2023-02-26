from .models import Product
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, IntegerField


class ProductSerializer(HyperlinkedModelSerializer):
    quantity = IntegerField(source="inventory.quantity", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "url", "name", "price", "quantity", "in_stock", "description",  "created_at", "updated_at"]
        read_only = ["created_at", "in_stock"]
