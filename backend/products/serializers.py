from pictures.models import Picture
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import IntegerField
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from rest_framework.serializers import SlugRelatedField

from .models import Product
from .models import ProductInventory


class ProductListSerializer(HyperlinkedModelSerializer):
    quantity = IntegerField(source="inventory.quantity")
    main_image = SlugRelatedField(many=False, read_only=True, slug_field="url")

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
    quantity = IntegerField(source="inventory.quantity", read_only=True, required=False)
    main_image = SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="url",
        required=False,
    )
    images = SlugRelatedField(
        many=True, read_only=True, slug_field="url", required=False
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
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class ProductCreateSerializer(ModelSerializer):
    quantity = IntegerField(source="inventory.quantity")
    main_image = PrimaryKeyRelatedField(
        many=False,
        queryset=Picture.objects.all(),
        allow_null=True,
    )
    images = PrimaryKeyRelatedField(many=True, queryset=Picture.objects.all())

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
        ]

    def create(self, validated_data):
        inventory = validated_data.pop("inventory")
        obj = super().create(validated_data)
        obj_inventory = ProductInventory.objects.get(product=obj)
        obj_inventory.quantity = inventory["quantity"]
        obj_inventory.save()
        return obj

    def update(self, instance, validated_data):
        if "inventory" in validated_data:
            inventory = validated_data.pop("inventory")
            instance = super().update(instance, validated_data)
            obj_inventory = ProductInventory.objects.get(product=instance)
            obj_inventory.quantity = inventory["quantity"]
            obj_inventory.save()
            return instance
        return super().update(instance, validated_data)


class ProductInventorySerializer(ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ["product_id", "quantity", "sold_qty", "created_at", "updated_at"]
