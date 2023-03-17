from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_200_OK
from django.contrib.auth import get_user_model
from .models import Article, ArticleCategory


class APITestCaseBase(APITestCase):

    fixtures = ["fixture.json"]

    def setUp(self):
        self.username = "demo"
        self.password = "demo1234"


class ArticleTestCase(APITestCaseBase):

    def setUp(self):
        super().setUp()
        self.admin = get_user_model().objects.get(username="demo")
        self.slug = "my_title"
        self.data = {
            "title": "My title",
            "slug": "test_title",
            "author": 1,
            "categories": [ "summer", "gold", "gift"]
        }

    def test_create_article_denied(self):
        response = self.client.post(reverse("article-list"), self.data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_publish_article_failed(self):
        response = self.client.post(reverse("article_publish", kwargs={"pk": self.slug}))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_article_detail_view(self):
        r = self.client.get(reverse("article-detail", kwargs={"pk": self.slug}))
        self.assertEqual(r.status_code, HTTP_200_OK)

    def test_create_and_publish_article_success(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse("article-list"), self.data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        article = Article.objects.get(slug=self.slug)
        self.assertNotEqual(article, None)
        response = self.client.post(reverse("article_publish", kwargs={"pk": self.slug}))
        self.assertEqual(response.status_code, HTTP_200_OK)


class CategoryTestCase(APITestCaseBase):

    def setUp(self):
        super().setUp()
        self.data = {
            "name": "my category"
        }

    def test_get_all_denied(self):
        r = self.client.get(reverse("article_categories"))
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_denied(self):
        r = self.client.post(reverse("article_categories"), data=self.data)
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_and_get_all_success(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.post(reverse("article_categories"), self.data)
        self.assertEqual(r.status_code, HTTP_201_CREATED)
        r = self.client.get(reverse("article_categories"))
        self.assertEqual(r.status_code, HTTP_200_OK)


class ArticleFilterTestCase(APITestCaseBase):

    def setUp(self):
        super().setUp()
        article = Article.objects.create(
            title="my_unique_test_title",
            slug="my_unique_test_title",
            is_published=True,
            author_id=1
        )
        winter = ArticleCategory.objects.get(name="winter")
        for_him = ArticleCategory.objects.get(name="for him")
        article.categories.add(winter, for_him)

    def test_is_published_true(self):
        r = self.client.get(reverse("article-list"), {"is_published": True})
        self.assertEqual(r.status_code, HTTP_200_OK)
        data = r.json()
        result = data["results"]
        first = result[0]
        self.assertNotEqual(0, data["count"])
        self.assertNotIn("slug", first)
        self.assertNotIn("is_published", first)
        self.assertIn("categories", first)
        self.assertTrue(
            all(
                map(
                    lambda x: bool(x["published_at"]),
                    result,
                )
            )
        )

    def test_is_published_false(self):
        r = self.client.get(reverse("article-list"), {"is_published": False})
        data = r.json()
        self.assertEqual(0, data["count"])

    def test_categories(self):
        r = self.client.get(reverse("article-list"), {"categories": ["winter", "for him"]})
        self.assertEqual(r.status_code, HTTP_200_OK)
        data = r.json()
        self.assertNotEqual(0, data["count"])
        first = data["results"][0]
        self.assertIn("categories", first)
        self.assertIn("winter", first["categories"])
        self.assertIn("for him", first["categories"])

    def test_is_published_admin(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.get(reverse("article-list"), {"is_published": False})
        self.assertEqual(r.status_code, HTTP_200_OK)
        data = r.json()
        result = data["results"]
        first = result[0]
        self.assertNotEqual(0, data["count"])
        self.assertIn("is_scheduled", first)
        self.assertIn("scheduled_at", first)
        self.assertIn("is_published", first)
        self.assertIn("slug", first)
        self.assertTrue(
            all(
                map(
                    lambda x: not bool(x["is_published"]),
                    result,
                )
            )
        )
