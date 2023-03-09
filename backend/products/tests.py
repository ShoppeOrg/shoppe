from django.test import TestCase
from .filters import NamedOrderingFilter


class FilterTestCase(TestCase):

    def test_get_ordering_value(self):
        o = NamedOrderingFilter(
            fields={
                "field1": "test1",
                "field2": "test2",
            },
        )
        self.assertEqual(o.get_ordering_value("test1.asc"), "field1")
        self.assertEqual(o.get_ordering_value("test1.desc"), "-field1")
        self.assertEqual(o.get_ordering_value("test.asc"), "test")
