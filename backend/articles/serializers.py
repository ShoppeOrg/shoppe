from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, CharField, SlugRelatedField
from .models import Article, ArticleCategory


class ArticleSerializer(HyperlinkedModelSerializer):
    categories = SlugRelatedField(
        slug_field="name",
        read_only=True,
        many=True,
    )
    author_fullname = CharField(source="author.fullname", read_only=True)

    class Meta:
        model = Article
        fields = ["url", "title", "author_fullname", "categories", "published_at"]


class ArticleDetailSerializer(ModelSerializer):

    categories = SlugRelatedField(
        slug_field="name",
        read_only=True,
        many=True,
    )
    author_fullname = CharField(source="author.fullname")

    class Meta:
        model = Article
        fields = ["title", "author_fullname", "categories", "data", "published_at"]


class ArticleCreateSerializer(ModelSerializer):
    categories = SlugRelatedField(
        slug_field="name",
        queryset=ArticleCategory.objects.all(),
        many=True,
    )

    class Meta:
        model = Article,
        fields = ["title", "slug", "categories", "author"]
