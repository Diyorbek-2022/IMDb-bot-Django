from django.urls import path

from Cinema.views import CheckCinemaCodeView

urlpatterns = [
    path("check-cinema-code/", CheckCinemaCodeView.as_view(), name="check_cinema_code"),
]
