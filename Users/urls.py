from django.contrib import admin
from django.urls import path, include
from Users import views   # agar Cinema modeli Users app ichida bo‘lsa

urlpatterns = [
    path("admin/", admin.site.urls),
    path("check-cinema-code/", views.check_cinema_code, name="check_cinema_code"),
]
