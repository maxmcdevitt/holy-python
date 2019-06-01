from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hp_app/', include('hp_app.urls')),
    path('admin/', admin.site.urls),
]

