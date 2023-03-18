from .models import Product, ProductInventory
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, IntegerField, SlugRelatedField


class ProductListSerializer(HyperlinkedModelSerializer):
    quantity = IntegerField(source="inventory.quantity")
    main_image = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="url"
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "url",
            "name",
            "price",
            "quantity",
            "main_image",
            "in_stock",
            "description",
            "created_at",
            "updated_at",
        ]


class ProductDetailSerializer(ModelSerializer):
    quantity = IntegerField(source="inventory.quantity", read_only=True)
    main_image = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="url"
    )
    images = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="url"
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "quantity",
            "in_stock",
            "main_image",
            "images",
            "description",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["created_at", "updated_at"]


class ProductInventorySerializer(ModelSerializer):

    class Meta:
        model = ProductInventory
        fields = ["product_id", "quantity", "sold_qty", "created_at", "updated_at"]