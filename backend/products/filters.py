from django_filters.rest_framework import FilterSet, NumberFilter, BooleanFilter, OrderingFilter


class NamedOrderingFilter(OrderingFilter):

    def get_ordering_value(self, param):
        param, ending = param.split(".")
        prefix = "-" if ending == "desc" else ""
        return prefix + self.param_map.get(param,param)


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr="gte")
    max_price = NumberFilter(field_name="price", lookup_expr="lte")
    in_stock = BooleanFilter(field_name="inventory__quantity", method="filter_in_stock")
    order_by = NamedOrderingFilter(
        fields={
            "inventory__sold_qty": "popular",
            "price": "price",
            "updated_at": "recent",
        },
        choices=(
            ("popular.desc", "by Popularity (DESC)"),
            ("price.asc", "by Price"),
            ("price.desc", "by Price (DESC)"),
            ("recent.desc", "by Recent added"),
        ),

    )

    def filter_in_stock(self, queryset, name, value):
        lookup_ex = "__".join([name, "exact"])
        if value:
            return queryset.exclude(**{lookup_ex: 0})
        return queryset.filter(**{lookup_ex: 0})