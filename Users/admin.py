from django.contrib import admin

from .forms import InfoForm, UserForm, FavoriteForm, ShowedForm
from .models import Info, User, Favorite, Showed


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    form = InfoForm
    list_display = ("id", "name", "type", "year", "rating", "age_limit")
    search_fields = ("name", "type")
    list_filter = ("type", "year", "age_limit")
    ordering = ("-year", "-rating")
    list_per_page = 20
    # date_hierarchy = "created_time"  # agar DateTimeField bo‘lsa ishlatish mumkin

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("name", "type", "year")
        }),
        ("Qo‘shimcha ma'lumotlar", {
            "fields": ("rating", "age_limit")
        }),
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm

    # Admin ro‘yxatda ko‘rinadigan ustunlar
    list_display = (
        "id", "full_name", "email", "phone_number",
        "is_active", "is_ban", "is_staff", "is_superuser",
        "created_time",
    )
    list_filter = (
        "is_active", "is_ban", "is_staff", "is_superuser", "created_time"
    )
    search_fields = ("full_name", "email", "phone_number")
    list_editable = ("is_active", "is_ban")
    ordering = ("-id",)
    list_per_page = 25

    # Admin forma sahifasida tartibli ko‘rinishi uchun bo‘linmalar
    fieldsets = (
        ("👤 Shaxsiy ma'lumotlar", {
            "fields": ("full_name", 'age', "email", "phone_number"),
            "description": "Foydalanuvchining asosiy identifikatsiya ma'lumotlari."
        }),
        ("⚙️ Tizim huquqlari", {
            "fields": ("is_active", "is_ban", "is_staff", "is_superuser"),
            "description": "Admin panel va tizimga kirish ruxsatlarini boshqarish."
        }),
        ("⏱ Vaqt ma'lumotlari", {
            "fields": ("created_time",),
            "classes": ("collapse",),  # collapse qilsak yopiq bo‘ladi, kerak bo‘lganda ochiladi
        }),
    )

    # O‘qib bo‘ladigan (readonly) maydonlar
    readonly_fields = ("created_time",)

    # Qo‘shimcha uslub: ma'lumotni tezroq topish uchun
    save_on_top = True  # saqlash tugmalari tepadayam ko‘rinadi

    # Qo‘shimcha vizual yaxshilash
    def get_queryset(self, request):
        """Optimallashtirilgan queryset ishlatish (agar kerak bo‘lsa)."""
        return super().get_queryset(request).select_related()

    def full_name_upper(self, obj):
        """Ismni katta harflarda chiqarish misoli."""
        return obj.full_name.upper()

    full_name_upper.short_description = "Full Name (Uppercase)"  # xohlasang list_displayga qo‘shib qo‘yasan


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    form = FavoriteForm
    list_display = ("id", "user", "get_cinema_name", "rating", "added_time")
    search_fields = ("user__full_name", "cinema__info__name")
    list_filter = ("rating", "added_time")
    ordering = ("-added_time",)
    date_hierarchy = "added_time"
    list_per_page = 20
    autocomplete_fields = ("user", "cinema")

    def get_cinema_name(self, obj):
        return obj.cinema.info.name

    get_cinema_name.short_description = "Cinema"


@admin.register(Showed)
class ShowedAdmin(admin.ModelAdmin):
    form = ShowedForm
    list_display = ("id", "user", "get_cinema_name", "showed_time")
    search_fields = ("user__full_name", "cinema__info__name")
    list_filter = ("showed_time",)
    ordering = ("-showed_time",)
    date_hierarchy = "showed_time"
    list_per_page = 20
    autocomplete_fields = ("user", "cinema")

    def get_cinema_name(self, obj):
        return obj.cinema.info.name

    get_cinema_name.short_description = "Cinema"
