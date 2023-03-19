from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path("", include("drfpasswordless.urls")),
    path("", include("products.urls")),
    path("", include("articles.urls")),
    path("", include("pictures.urls")),
]
