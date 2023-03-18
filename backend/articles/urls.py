from django.urls import path

from .views import ArticleCategoryListCreateAPIView
from .views import ArticleListCreateAPIView
from .views import ArticlePublishAPIView
from .views import ArticleRetrieveAPIView


urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path(
        "articles/categories/",
        ArticleCategoryListCreateAPIView.as_view(),
        name="article_categories",
    ),
    path(
        "articles/<slug:pk>/", ArticleRetrieveAPIView.as_view(), name="article-detail"
    ),
    path(
        "articles/<slug:pk>/publish/",
        ArticlePublishAPIView.as_view(),
        name="article_publish",
    ),
]
