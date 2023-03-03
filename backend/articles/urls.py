from django.urls import path
from .views import ArticleListAPIView, ArticleRetrieveAPIView, ArticleCategoryListAPIView, ArticlePublishAPIView


urlpatterns = [
    path("articles/", ArticleListAPIView.as_view()),
    path("articles/<slug:slug>", ArticleRetrieveAPIView.as_view(), name="article-detail"),
    path("articles/categories/", ArticleCategoryListAPIView.as_view()),
    path("articles/<slug:pk>/publish/", ArticlePublishAPIView.as_view(), name="article-publish")
]