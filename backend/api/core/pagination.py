from rest_framework.pagination import PageNumberPagination


class ExtendedPageNumberPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    page_size = 10
    max_page_size = 100
