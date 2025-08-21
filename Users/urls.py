from django.urls import path

from .views import UserListView, CheckCinemaCodeView, UserDetailView, UserCreateView

urlpatterns = [
    path("check-cinema-code/", CheckCinemaCodeView.as_view(), name="check_cinema_code"),
    path('user/', UserListView.as_view(), name='user_list'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/<str:id>/', UserDetailView.as_view(), name='user_detail'),
    path('user/update/<str:id>/', UserDetailView.as_view(), name='user_update'),
]
