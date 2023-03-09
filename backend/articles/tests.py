from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_200_OK
from django.contrib.auth import get_user_model
from .models import Article


class ArticleTestCase(APITestCase):

    def setUp(self):
        self.admin = get_user_model().objects.get(username="demo")
        self.username = "demo"
        self.password = "demo1234"
        self.slug = "test_title"
        self.data = {
            "title": "My title",
            "slug": self.slug,
            "author": 1,
            "categories": ["summer", "autumn", "for her"]
        }

    def test_create_article_denied(self):
        response = self.client.post(reverse("article-list"), data=self.data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_publish_article_failed(self):
        response = self.client.post(reverse("article_publish", pk=self.slug))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_article_detail_view(self):
        r = self.client.get(reverse("article-detail", pk=self.slug))
        self.assertEqual(r.status_code, HTTP_200_OK)

    def test_create_article_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse("article-list"), data=self.data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        article = Article.objects.get(slug=self.slug)
        self.assertNotEqual(article, None)

    def test_publish_article_success(self):
        response = self.client.post(reverse("article_publish", pk=self.slug))
        self.assertEqual(response.status_code, HTTP_200_OK)


class CategoryTestCase(APITestCase):

    def setUp(self):
        self.username = "demo"
        self.password = "demo1234"
        self.data = {
            "category": "my test category"
        }

    def test_get_all_denied(self):
        r = self.client.get(reverse("article_categories"))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_denied(self):
        r = self.client.post(reverse("article_categories"), data=self.data)
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_success(self):
        self.client.login(usernam=self.username, password=self.password)
        r = self.client.post(reverse("article_categories"), data=self.data)
        self.assertEqual(r.status_code, HTTP_201_CREATED)

    def test_get_all_success(self):
        r = self.client.get(reverse("article_categories"))
        self.assertEqual(r.status_code, HTTP_200_OK)


class ArticleFilterTestCase(APITestCase):

    def test_get_all(self):
        r = self.client.get(reverse("article-list"))
        data = r.json()
        self.assertIn("next", data)
        self.assertIn("previous", data)
        self.assertIn("result", data)
        self.assertEqual(10, len(data["result"]))

    def test_page_size(self):
        r = self.client.get(reverse("article-list"), {"page_size": 30})
        data = r.json()
        self.assertEqual(30, len(data["result"]))
        r = self.client.get(reverse("article-list"), {"page_size": 5})
        data = r.json()
        self.assertEqual(10, len(data["result"]))
        r = self.client.get(reverse("article-list"), {"page_size": 120})
        data = r.json()
        self.assertEqual(100, len(data["result"]))

    def test_in_stock(self):
        r = self.client.get(reverse("article-list"), {"in_stock": True})
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
        r = self.client.get(reverse("article-list"), {"in_stock": False})
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
        r = self.client.get(reverse("article-list"), {"min_price": 10, "max_price": 500})
        data = r.json()
        self.assertEqual(r.status_code, HTTP_200_OK)
        self.assertTrue(len(data["result"]) > 0)
        r = self.client.get(reverse("article-list"), {"min_price": 10, "max_price": -500})
        self.assertNotEqual(r.status_code, HTTP_200_OK)
        r = self.client.get(reverse("article-list"), {"min_price": 10, "max_price": 0})
        self.assertNotEqual(r.status_code, HTTP_200_OK)


