from django.utils import timezone
from rest_framework.serializers import CharField
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from rest_framework.serializers import Serializer
from rest_framework.serializers import SlugRelatedField
from rest_framework.serializers import ValidationError
from user.models import User

from .models import Article
from .models import ArticleCategory


class AuthorInfo(Serializer):
    author_fullname = CharField(source="author.fullname", read_only=True)
    author_username = CharField(source="author.username", read_only=True)


class ArticleSerializer(HyperlinkedModelSerializer, AuthorInfo):
    categories = PrimaryKeyRelatedField(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Article
        fields = [
            "url",
            "title",
            "author_fullname",
            "author_username",
            "categories",
            "published_at",
        ]


class ArticleDetailSerializer(ModelSerializer, AuthorInfo):
    class Meta:
        model = Article
        fields = [
            "title",
            "author_fullname",
            "author_username",
            "categories",
            "data",
            "published_at",
        ]


class ArticleCreateSerializer(ModelSerializer):
    categories = PrimaryKeyRelatedField(
        queryset=ArticleCategory.objects.all(),
        many=True,
    )
    author = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Article
        fields = [
            "title",
            "slug",
            "categories",
            "author",
            "data",
            "is_published",
            "scheduled_at",
        ]

    def validate_scheduled_at(self, value):
        if value and value < timezone.now():
            raise ValidationError("Field 'scheduled_at' should be a date in future.")
        return value

    def create(self, validated_data):
        if validated_data["is_published"]:
            validated_data["scheduled_at"] = None
        return super().create(validated_data)


class ArticleFullDetailSerializer(ArticleSerializer):
    class Meta:
        model = Article
        fields = [
            "url",
            "title",
            "slug",
            "author_fullname",
            "author_username",
            "data",
            "categories",
            "is_published",
            "published_at",
            "is_scheduled",
            "scheduled_at",
            "created_at",
            "updated_at",
        ]


class ArticleCategorySerializer(ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ["name"]
