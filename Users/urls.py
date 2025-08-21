from django.urls import path

from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path("", UserListView.as_view(), name='user_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<str:id>/', UserDetailView.as_view(), name='user_detail'),
    path('update/<str:id>/', UserDetailView.as_view(), name='user_update'),
]
