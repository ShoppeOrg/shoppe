from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from pictures.models import Picture
from django.core.files import File
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_200_OK
from pathlib import Path
import os


class APITestCaseBase(APITestCase):

    fixtures = ['fixture.json']
    
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        path = Path(__file__).resolve().parent
        cls.image_name = "test_image1.png"
        cls.picture_path = os.path.join(path, "test_data", cls.image_name)
        
        
class ModelTestCase(APITestCaseBase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.obj = Picture.objects.create(
            title="some explanation about picture",
            picture=File(open(cls.picture_path, "rb"))
        )

    def test_url(self):
        print(self.obj.picture.url)
        self.assertTrue(
            self.obj.picture.url.endswith("png")
        )

    def test_name(self):
        self.assertNotEqual(self.obj.picture.name, self.image_name)


class PictureViewTestCase(APITestCaseBase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.username = "demo"
        cls.password = "demo1234"

    def test_picture_upload_access_denied(self):
        r = self.client.post(reverse("image_upload"), {
                "title": "some title",
                "picture": File(open(self.picture_path, "rb"))
            }
        )
        self.assertEqual(r.status_code, HTTP_401_UNAUTHORIZED)

    def test_picture_upload(self):
        self.client.login(username=self.username, password=self.password)
        r = self.client.post(reverse("image_upload"), {
            "title": "some title",
            "picture": File(open(self.picture_path, "rb"))
            }
        )
        self.assertEqual(r.status_code, HTTP_201_CREATED)
        data = r.json()
        self.assertIn("url", data)
        self.assertIn("id", data)
        self.assertIn("title", data)
