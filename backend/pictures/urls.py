from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import PictureUpload

urlpatterns = [
    path("images/upload/", PictureUpload.as_view(), name="image_upload")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
