from django import forms

from .models import Cinema


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = "__all__"
        widgets = {
            "cinema_url": forms.TextInput(attrs={
                "placeholder": "🎬 Enter cinema file_id or URL (e.g. https://example.com/cinema.mp4 OR AgADBAADb6oxG...)",
                "class": "form-control shadow-sm rounded px-3",
                "title": "Enter cinema file_id or Telegram URL",
                "maxlength": 255,
                "autocomplete": "off"
            }),
            "cinema_code": forms.TextInput(attrs={
                "placeholder": "🔑 Unique cinema code...",
                "class": "form-control shadow-sm rounded px-3 fw-bold text-uppercase",
                "title": "Enter a unique code for the cinema",
                "maxlength": 20,
                "autocomplete": "off",
                "id": "id_cinema_code"  # AJAX uchun kerak
            }),
            "next": forms.NumberInput(attrs={
                "placeholder": "➡️ Next cinema ID",
                "class": "form-control shadow-sm rounded text-center fw-semibold",
                "min": 1,
                "step": 1,
                "title": "Enter the ID of the next cinema if available"
            }),
            "previous": forms.NumberInput(attrs={
                "placeholder": "⬅️ Previous cinema ID",
                "class": "form-control shadow-sm rounded text-center fw-semibold",
                "min": 1,
                "step": 1,
                "title": "Enter the ID of the previous cinema if available"
            }),
        }

    class Media:
        js = ("js/cinema_code_check.js",)
