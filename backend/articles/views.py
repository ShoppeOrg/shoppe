from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from django.db.models import ObjectDoesNotExist
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


class ArticlePublishAPIView(APIView):

    def post(self, request, pk=None):
        try:
            article = Article.objects.get(pk=pk)
            article.is_published = True
            article.save()
        except ObjectDoesNotExist:
            return Response(
                {
                    "detail": {
                        "info": "Article with given slug not found",
                        "pk": pk
                    }
                },
                status=HTTP_404_NOT_FOUND
            )
        return Response(
            {
                "detail": "Article has been published."
            },
            status=200
        )


