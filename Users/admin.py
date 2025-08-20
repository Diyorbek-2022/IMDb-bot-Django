from django.contrib import admin

from .forms import InfoForm, UserForm, FavoriteForm, ShowedForm, CinemaForm
from .models import Info, Cinema, User, Favorite, Showed


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    form = CinemaForm
    list_display = ("id", "get_name", "get_age_limit", "cinema_code", "added_time")
    list_filter = ("info__age_limit", "added_time")
    search_fields = ("info__name", "cinema_code")

    def get_name(self, obj):
        return obj.info.name if obj.info else "No info"
    get_name.short_description = "Name"

    def get_age_limit(self, obj):
        return obj.info.age_limit if obj.info else "No info"
    get_age_limit.short_description = "Age Limit"



@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    form = InfoForm
    list_display = ("id", "name", "type", "year", "rating", "age_limit")
    search_fields = ("name", "type")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ("id", "full_name", "email", "phone_number", "is_active", "is_ban")
    list_filter = ("is_active", "is_ban", "is_staff", "is_superuser")
    search_fields = ("full_name", "email", "phone_number")
    list_editable = ("is_active", "is_ban")  # checkbox bilan admin panelda o'zgartirish mumkin


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    form = FavoriteForm
    list_display = ("id", "user", "get_cinema_name", "rating", "added_time")
    search_fields = ("user__full_name", "cinema__info__name")

    def get_cinema_name(self, obj):
        return obj.cinema.info.name
    get_cinema_name.short_description = "Cinema"


@admin.register(Showed)
class ShowedAdmin(admin.ModelAdmin):
    form = ShowedForm
    list_display = ("id", "user", "get_cinema_name", "showed_time")
    search_fields = ("user__full_name", "cinema__info__name")

    def get_cinema_name(self, obj):
        return obj.cinema.info.name
    get_cinema_name.short_description = "Cinema"
