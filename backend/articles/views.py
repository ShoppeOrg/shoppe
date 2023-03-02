from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser
from .models import Article, ArticleCategory
from .serializers import ArticleSerializer, ArticleDetailSerializer, ArticleCategorySerializer, ArticleCreateSerializer


class ArticleListAPIView(ListCreateAPIView):
    queryset = Article.objects.filter(is_published=True).prefetch_related("author", "categories")

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser(), ]
        return super().get_permissions()
    def get_serializer_class(self):
        if self.request.method == "POST":
            return ArticleCreateSerializer
        return ArticleSerializer


class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.filter(is_published=True).prefetch_related("author", "categories")
    serializer_class = ArticleDetailSerializer


class ArticleCategoryListAPIView(ListCreateAPIView):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
    permission_classes = (IsAdminUser, )

