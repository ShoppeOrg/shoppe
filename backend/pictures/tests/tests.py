from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from pictures.models import Picture
from django.core.files import File
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_200_OK


class ModelTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.image_name = "test_image1.png"
        cls.obj = Picture.objects.create(
            title="some explanation about picture",
            picture=File(open("test_data/test_image1.png", "rb"))
        )

    def test_url(self):
        self.assertTrue(
            self.obj.url.startswith("http")
        )
        r = self.client.get(self.obj.url)
        self.assertEqual(r.status_code, HTTP_200_OK)

    def test_name(self):
        self.assertNotEqual(self.obj.name, self.image_name)


class PictureViewTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.image = "test_data/test_image1.png"
        cls.username = "demo"
        cls.password = "demo1234"

    def test_picture_upload_access_denied(self):
        r = self.client.post(reverse("image_upload"), {
                "title": "some title",
                "picture": File(open(self.image, "rb"))
            }
        )
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_picture_upload(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.post(reverse("image_upload"), {
            "title": "some title",
            "picture": File(open(self.image, "rb"))
            }
        )
        self.assertEqual(r.status_code, HTTP_201_CREATED)
        data = r.json()
        self.assertIn("url", data)
        self.assertIn("id", data)
        self.assertIn("title", data)
        r = self.client.get(data["url"])
        self.assertEqual(r.status_code, HTTP_200_OK)
