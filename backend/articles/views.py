from rest_framework.generics import ListAPIView
from .models import Article
from .serializers import ArticleSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.prefetch_related("author", "categories")
    serializer_class = ArticleSerializer
