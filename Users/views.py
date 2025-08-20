from django.http import JsonResponse
from .models import Cinema

def check_cinema_code(request):
    code = request.GET.get("cinema_code", "").strip()
    is_taken = Cinema.objects.filter(cinema_code=code).exists()
    return JsonResponse({"is_taken": is_taken})
