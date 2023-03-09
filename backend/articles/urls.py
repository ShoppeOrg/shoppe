from django.urls import path
from .views import ArticleListAPIView, ArticleRetrieveAPIView, ArticleCategoryListAPIView, ArticlePublishAPIView


urlpatterns = [
    path("articles/", ArticleListAPIView.as_view(), name="article-list"),
    path("articles/<slug:pk>/", ArticleRetrieveAPIView.as_view(), name="article-detail"),
    path("articles/categories/", ArticleCategoryListAPIView.as_view(), name="article_categories"),
    path("articles/<slug:pk>/publish/", ArticlePublishAPIView.as_view(), name="article_publish")
]
