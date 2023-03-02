from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Article
from .serializers import ArticleSerializer, ArticleDetailSerializer


class ArticleListAPIView(ListCreateAPIView):
    queryset = Article.objects.filter(is_published=True).prefetch_related("author", "categories")
    serializer_class = ArticleSerializer


class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.filter(is_published=True).prefetch_related("author", "categories")
    serializer_class = ArticleDetailSerializer

