import json

from django.core.exceptions import ValidationError
from drfpasswordless.utils import create_callback_token_for_user
from pictures.models import Picture
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.test import APITestCase

from .filters import NamedOrderingFilter
from .models import Product
from .models import ProductInventory
from .models import Review


class APITestCaseBase(APITestCase):
    fixtures = ["fixture.json"]


class FilterTestCase(APITestCaseBase):
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


class ProductFilterTestCase(APITestCaseBase):
    def test_get_all(self):
        r = self.client.get(reverse("product-list"))
        data = r.json()
        self.assertIn("next", data)
        self.assertIn("previous", data)
        self.assertIn("results", data)
        self.assertEqual(10, len(data["results"]))

    def test_page_size(self):
        r = self.client.get(reverse("product-list"), {"page_size": 30})
        data = r.json()
        self.assertEqual(30, len(data["results"]))
        r = self.client.get(reverse("product-list"), {"page_size": -2})
        data = r.json()
        self.assertEqual(10, len(data["results"]))
        r = self.client.get(reverse("product-list"), {"page_size": 5})
        data = r.json()
        self.assertEqual(5, len(data["results"]))
        r = self.client.get(reverse("product-list"), {"page_size": 120})
        data = r.json()
        self.assertEqual(100, len(data["results"]))

    def test_in_stock(self):
        r = self.client.get(reverse("product-list"), {"in_stock": True})
        data = r.json()
        result = data["results"]
        self.assertTrue(all(v["in_stock"] for v in result))
        r = self.client.get(reverse("product-list"), {"in_stock": False})
        data = r.json()
        result = data["results"]
        self.assertFalse(any(v["in_stock"] for v in result))

    def test_min_max_price(self):
        r = self.client.get(
            reverse("product-list"), {"min_price": 10, "max_price": 500}
        )
        data = r.json()
        self.assertEqual(r.status_code, HTTP_200_OK)
        self.assertTrue(len(data["results"]) > 0)
        r = self.client.get(
            reverse("product-list"), {"min_price": 10, "max_price": -500}
        )
        self.assertEqual(r.status_code, HTTP_200_OK)
        self.assertEqual(0, len(r.json()["results"]))
        r = self.client.get(reverse("product-list"), {"min_price": 10, "max_price": 0})
        self.assertEqual(r.status_code, HTTP_200_OK)
        self.assertEqual(0, len(r.json()["results"]))


class ProductTestCase(APITestCaseBase):
    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "name": "some test name",
            "description": "some interesting description",
            "price": 20.10,
            "quantity": 5,
            "main_image": 1,
            "images": [1, 2, 3],
        }
        cls.username = "demo"
        cls.password = "demo1234"
        product = Product.objects.get(pk=1)
        pictures = Picture.objects.filter(id__in=[1, 2, 3])
        product.images.add(*pictures)

    def test_access_denied(self):
        r = self.client.post(reverse("product-list"), self.data)
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        r = self.client.patch(reverse("product-detail", {1}), {"name": "another name"})
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        r = self.client.put(reverse("product-list"), self.data)
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        r = self.client.delete(reverse("product-detail", {1}))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_list_and_detail_view(self):
        r = self.client.get(reverse("product-list"))
        self.assertEqual(r.status_code, HTTP_200_OK)
        result = r.json()["results"]
        self.assertNotIn("images", result[0])
        self.assertIn("main_image", result[0])
        self.assertIn("url", result[0])
        r = self.client.get(reverse("product-detail", {1}))
        self.assertEqual(r.status_code, HTTP_200_OK)
        result = r.json()
        self.assertNotIn("url", result)
        self.assertIn("images", result)
        self.assertNotEqual(0, len(result["images"]))

    def test_create_product(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.post(reverse("product-list"), self.data)
        self.assertEqual(r.status_code, HTTP_201_CREATED)
        result = r.json()
        self.assertIn("images", result)
        self.assertNotEqual(0, len(result["images"]))

    def test_update_product(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.get(reverse("product-detail", {1}))

        data_patch = {"images": [4, 5, 6]}
        data_put = r.json()
        data_put["images"] = data_patch["images"]

        r = self.client.put(
            reverse("product-detail", {1}),
            json.dumps(data_patch),
            content_type="application/json",
        )
        self.assertEqual(r.status_code, HTTP_400_BAD_REQUEST)

        r_put = self.client.put(
            reverse("product-detail", {1}),
            json.dumps(data_put),
            content_type="application/json",
        )
        r_patch = self.client.patch(
            reverse("product-detail", {1}),
            json.dumps(data_patch),
            content_type="application/json",
        )
        for r in [r_patch, r_put]:
            data = r.json()
            self.assertEqual(r.status_code, HTTP_200_OK, r.content)
            self.assertIn("images", data)
            self.assertEqual(3, len(data["images"]))
            self.assertIn(4, data["images"])
            self.assertIn(5, data["images"])
            self.assertIn(6, data["images"])


class InventoryTestCase(APITestCaseBase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "demo"
        cls.password = "demo1234"
        cls.data = {
            "quantity": 100,
            "sold_qty": 1000,
        }

    def test_inventory_access_denied(self):
        r = self.client.get(reverse("product_inventory", {1}))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        r = self.client.put(reverse("product_inventory", {1}), data=self.data)
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_get_and_update_inventory(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.get(reverse("product_inventory", {1}))
        self.assertEqual(r.status_code, HTTP_200_OK)
        result = r.json()
        self.assertEqual(1, result["product_id"])
        self.assertIn("sold_qty", result)
        self.assertIn("quantity", result)
        r = self.client.put(reverse("product_inventory", {1}), data=self.data)
        result = r.json()
        for key in self.data:
            self.assertIn(key, result)
            self.assertEqual(result[key], self.data[key])


class ModelsAPITestCase(APITestCaseBase):
    def test_inventory_created(self):
        obj = Product(name="abs_unique_name", price=101)
        obj.save()
        self.assertNotEqual(obj.id, None)
        obj_inventory = ProductInventory.objects.get(product=obj)
        self.assertNotEqual(obj_inventory, None)

    def test_validation_errors(self):
        obj = Product.objects.get(pk=1)
        obj_inventory = ProductInventory.objects.get(product=obj)
        with self.assertRaises(ValidationError):
            obj.price = -100
            obj.clean_fields()
            obj.save()

        with self.assertRaises(ValidationError):
            obj_inventory.quantity = -100
            obj.clean_fields()
            obj_inventory.save()

        with self.assertRaises(ValidationError):
            obj_inventory.sold_qty = -100
            obj.clean_fields()
            obj_inventory.save()


class ReviewAPITestCase(APITestCaseBase):
    @classmethod
    def setUpTestData(cls):
        cls.valid_data = {
            "user": 1,
            "product": 1,
            "rating": 2,
            "comment": "not a number",
        }
        Review.objects.create(
            user_id=1, product_id=1, rating=3, description="Not bad.", is_published=True
        )
        Review.objects.create(
            user_id=2,
            products_id=1,
            rating=5,
            description="Amazing!",
            is_published=True,
        )
        cls.token = "b0097509c392078fde5062bdd2c3ef6e98ca9af9"

    def test_not_authorized(self):
        r = self.client.post(reverse("product_review"), self.valid_data)
        self.assertEqual(r.status_code, HTTP_400_BAD_REQUEST, r.content)

    def test_GET_method_not_authorized(self):
        r = self.client.get(reverse("product_review"))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED, r.content)

    def test_create_success(self):
        r = self.client.post(
            reverse("product_review"),
            self.valid_data,
            AUTHORIZATION=f"Token {self.token}",
        )
        self.assertEqual(r.status_code, HTTP_201_CREATED, r.content)
        self.client.login(username="demo", password="demo1234")
        r = self.client.post(reverse("product_review"), self.valid_data)
        self.assertEqual(r.status_code, HTTP_201_CREATED, r.content)

    def test_reviews_in_product(self):
        r = self.client.get(reverse("product-detail", {1}))
        self.assertEqual(r.status_code, HTTP_200_OK, r.content)
        data = r.json()
        self.assertIn("reviews", data)
        self.assertNotEqual(0, len(data["reviews"]))
        self.assertTrue(review["is_published"] for review in data["reviews"])
        review = data["reviews"][0]
        for key in ["username", "rating", "comment", "is_published", "created_at"]:
            self.assertIn(key, review)

    def test_publish_review(self):
        review = Review.objects.create(**self.valid_data)
        self.assertFalse(review.is_published)
        r = self.client.post(reverse("product_review_publish", {review.id}))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        self.client.login(username="demo", password="demo1234")
        r = self.client.post(reverse("product_review_publish", {review.id}))
        self.assertEqual(r.status_code, HTTP_200_OK)
        self.assertTrue(review.is_published)

    def test_list_reviews(self):
        r = self.client.get(reverse("product_review"))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)
        self.client.login(username="demo", password="demo1234")
        r = self.client.get(reverse("product_review"))
        self.assertEqual(r.status_code, HTTP_200_OK)
        r = self.client.get(
            reverse("product_review"), AUTHORIZATION=f"Token {self.token}"
        )
        self.assertEqual(r.status_code, HTTP_403_FORBIDDEN)

    def test_user_and_auth_token_are_the_same(self):
        raise NotImplementedError()
