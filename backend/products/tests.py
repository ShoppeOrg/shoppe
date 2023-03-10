from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from .filters import NamedOrderingFilter
from .models import Product, ProductInventory
from django.core.exceptions import ValidationError

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


class ProductTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "name": "some test name",
            "description": "some interesting description",
            "price": 20.10,
            "quantity": 5,
            "main_image": 1,
            "images": [1,2,3]
        }
        cls.username = "demo"
        cls.password = "demo1234"

    def test_access_denied(self):
        r = self.client.post(reverse("product-list"), self.data)
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        r = self.client.patch(reverse("product-detail", pk=1), {
            "name": "another name"
        })
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        r = self.client.put(reverse("product-list"), self.data)
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        r = self.client.delete(reverse("product-detail", pk=1))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_list_and_detail_view(self):
        r = self.client.get(reverse("product-list"))
        self.assertEqual(r.status_code, HTTP_200_OK)
        result = r.json()["result"]
        self.assertNotIn("images", result[0])
        self.assertIn("main_image", result[0])
        self.assertIn("url", result[0])
        r = self.client.get(reverse("product-detail"), pk=1)
        self.assertEqual(r.status_code, HTTP_200_OK)
        result = r.json()
        self.assertNotIn("url", result)
        self.assertIn("images", result)
        response_image = self.client.get(result["images"][0])
        self.assertEqual(response_image.status_code, HTTP_200_OK)
        response_image = self.client.get(result["main_image"])
        self.assertEqual(response_image.status_code, HTTP_200_OK)

    def test_create_product(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.post(reverse("product-list"), self.data)
        self.assertEqual(r.status_code, HTTP_201_CREATED)
        result = r.json()
        self.assertIn("images", result)
        self.assertNotEqual(0, len(result["images"]))


class InventoryTestCase(APITestCase):

    def setUpTestData(cls):
        cls.username = "demo"
        cls.password = "demo1234"
        cls.data = {
            "quantity": 100,
            "sold_qty": 1000,
        }

    def test_inventory_access_denied(self):
        r = self.client.get(reverse("product_inventory", pk=1))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        r = self.client.put(reverse("product_inventory", pk=1), self.data)
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_get_and_update_inventory(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.get(reverse("product_inventory", pk=1))
        self.assertEqual(r.status_code, HTTP_200_OK)
        result = r.json()
        self.assertEqual(1, result["product_id"])
        self.assertIn("sold_qty", result)
        self.assertIn("quantity", result)
        r = self.client.put(reverse("product_inventory", pk=1), self.data)
        result = r.json()
        for key in self.data:
            self.assertIn(key, result)
            self.assertEqual(result[key], self.data[key])


class ModelsAPITestCase(APITestCase):

    def test_inventory_created(self):
        obj = Product(
            name="abs_unique_name",
            price=101
        )
        obj.save()
        self.assertNotEqual(obj.id, None)
        obj_inventory = ProductInventory.objects.get(product=obj)
        self.assertNotEqual(obj_inventory, None)

    def test_validation_errors(self):
        obj = Product.objects.get(pk=1)
        obj_inventory = ProductInventory.objects.get(product=obj)
        with self.assertRaises(ValidationError):
            obj.price = -100
            obj.save()

        with self.assertRaises(ValidationError):
            obj_inventory.quantity = -100
            obj_inventory.save()

        with self.assertRaises(ValidationError):
            obj_inventory.sold_qty = -100
            obj_inventory.save()
