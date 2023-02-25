from .models import Product
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "amount", "in_stock", "description",  "created_at", "updated_at"]
        read_only = ["created_at", "in_stock"]
