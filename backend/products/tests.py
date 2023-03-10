from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from .filters import NamedOrderingFilter


class FilterTestCase(APITestCase):

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


class ProductFilterTestCase(APITestCase):

    def test_get_all(self):
        r = self.client.get(reverse("product-list"))
        data = r.json()
        self.assertIn("next", data)
        self.assertIn("previous", data)
        self.assertIn("result", data)
        self.assertEqual(10, len(data["result"]))

    def test_page_size(self):
        r = self.client.get(reverse("product-list"), {"page_size": 30})
        data = r.json()
        self.assertEqual(30, len(data["result"]))
        r = self.client.get(reverse("product-list"), {"page_size": 5})
        data = r.json()
        self.assertEqual(10, len(data["result"]))
        r = self.client.get(reverse("product-list"), {"page_size": 120})
        data = r.json()
        self.assertEqual(100, len(data["result"]))

    def test_in_stock(self):
        r = self.client.get(reverse("product-list"), {"in_stock": True})
        data = r.json()
        result = data["result"]
        self.assertTrue(
            all(
                map(
                    lambda x: x["in_stock"],
                    result,
                )
            )
        )
        r = self.client.get(reverse("product-list"), {"in_stock": False})
        data = r.json()
        result = data["result"]
        self.assertFalse(
            any(
                map(
                    lambda x: x["in_stock"],
                    result,
                )
            )
        )

    def test_min_max_price(self):
        r = self.client.get(reverse("product-list"), {"min_price": 10, "max_price": 500})
        data = r.json()
        self.assertEqual(r.status_code, HTTP_200_OK)
        self.assertTrue(len(data["result"]) > 0)
        r = self.client.get(reverse("product-list"), {"min_price": 10, "max_price": -500})
        self.assertNotEqual(r.status_code, HTTP_200_OK)
        r = self.client.get(reverse("product-list"), {"min_price": 10, "max_price": 0})
        self.assertNotEqual(r.status_code, HTTP_200_OK)
