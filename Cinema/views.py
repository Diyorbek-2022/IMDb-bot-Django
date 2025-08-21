from rest_framework import generics
from rest_framework.response import Response

from .models import Cinema


class CheckCinemaCodeView(generics.GenericAPIView):
    queryset = Cinema.objects.all()

    def get(self, request, *args, **kwargs):
        code = request.GET.get("cinema_code", "").strip()
        is_taken = self.get_queryset().filter(cinema_code=code).exists()
        return Response({"is_taken": is_taken})
