from django_filters.rest_framework import FilterSet, BooleanFilter


class ArticleFilter(FilterSet):

    is_published = BooleanFilter(field_name="is_published")