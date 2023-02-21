from .models import Product
from rest_framework.serializers import ModelSerializer

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'amount', 'description', 'created_at', 'updated_at']