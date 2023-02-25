from django_filters.rest_framework import FilterSet, NumberFilter, BooleanFilter

class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr="gte")
    max_price = NumberFilter(field_name="price", lookup_expr="lte")
    in_stock = BooleanFilter(field_name="amount", method="filter_in_stock")

    def filter_in_stock(self, queryset, name, value):
        lookup_ex = "__".join([name, "exact"])
        if value:
            return queryset.exclude(**{lookup_ex: 0})
        return queryset.filter(**{lookup_ex: 0})