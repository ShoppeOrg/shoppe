from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('drfpasswordless.urls')),
    path('', include('products.urls')),
    path('', include('articles.urls'))
]
 