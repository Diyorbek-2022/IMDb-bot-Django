from django.contrib import admin
from .forms import CinemaForm
from .models import Cinema


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    form = CinemaForm
    list_display = ("id", "get_name", "get_age_limit", "cinema_code", "added_time")
    list_filter = ("info__age_limit", "added_time")
    search_fields = ("info__name", "cinema_code")
    ordering = ("-added_time",)  # eng yangi kinolar yuqorida
    list_per_page = 20  # bir sahifada 20ta obyekt
    readonly_fields = ("added_time",)  # qo'lda o'zgartirib bo'lmaydi

    # Formani guruhlash
    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("info", "cinema_code")
        }),
        ("Qo'shimcha ma'lumotlar", {
            "fields": ("added_time",),
            "classes": ("collapse",)  # collapse bo'lib ochiladi
        }),
    )

    def get_name(self, obj):
        return obj.info.name if obj.info else "No info"
    get_name.short_description = "Name"
    get_name.admin_order_field = "info__name"  # tartiblash uchun

    def get_age_limit(self, obj):
        return obj.info.age_limit if obj.info else "No info"
    get_age_limit.short_description = "Age Limit"
    get_age_limit.admin_order_field = "info__age_limit"
