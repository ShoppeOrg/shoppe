from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.urls import path

from .views import PictureUpload

urlpatterns = [
    path("images/upload/", PictureUpload.as_view(), name="image_upload")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
