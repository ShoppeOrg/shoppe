from django_filters.rest_framework import FilterSet, BooleanFilter, ModelMultipleChoiceFilter
from .models import ArticleCategory


class ArticleFilter(FilterSet):

    is_published = BooleanFilter(field_name="is_published")
    categories = ModelMultipleChoiceFilter(queryset=ArticleCategory.objects.all())
