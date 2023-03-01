from rest_framework.serializers import HyperlinkedModelSerializer, CharField
from .models import Article


class ArticleSerializer(HyperlinkedModelSerializer):

    author_fullname = CharField(source="author.fullname")

    class Meta:
        model = Article
        fields = [ "title", "author_fullname"]