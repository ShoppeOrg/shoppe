from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drfpasswordless.urls')),
    path('', include('products.urls')),
 ]
 