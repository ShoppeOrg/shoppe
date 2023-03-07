from django.urls import path, include
from django.contrib import admin
from django.conf import  settings
from django.conf.urls.static import static
urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('drfpasswordless.urls')),
    path('', include('products.urls')),
    path('', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
