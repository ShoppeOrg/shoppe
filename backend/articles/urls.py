from django.urls import path
from .views import ArticleListAPIView, ArticleRetrieveAPIView, ArticleCategoryListAPIView


urlpatterns = [
    path("articles/", ArticleListAPIView.as_view()),
    path("articles/<slug:slug>", ArticleRetrieveAPIView.as_view(), name="article-detail"),
    path("articles/categories/", ArticleCategoryListAPIView.as_view())
]