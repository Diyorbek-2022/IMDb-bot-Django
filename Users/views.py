from django.http import JsonResponse
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Cinema, User
from .serializers import UserSerializer


def check_cinema_code(request):
    code = request.GET.get("cinema_code", "").strip()
    is_taken = Cinema.objects.filter(cinema_code=code).exists()
    return JsonResponse({"is_taken": is_taken})


class CheckCinemaCodeView(generics.GenericAPIView):
    queryset = Cinema.objects.all()

    def get(self, request, *args, **kwargs):
        code = request.GET.get("cinema_code", "").strip()
        is_taken = self.get_queryset().filter(cinema_code=code).exists()
        return Response({"is_taken": is_taken})


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        lookup_value = self.kwargs.get("id")
        if lookup_value.isdigit() is not True:
            raise NotFound("User not found")
        try:
            return User.objects.get(pk=lookup_value)
        except User.DoesNotExist:
            try:
                return User.objects.get(user_id=lookup_value)
            except User.DoesNotExist:
                raise NotFound("User not found")

# class UserCreateView(generics.CreateAPIView):
class UserUpadateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer