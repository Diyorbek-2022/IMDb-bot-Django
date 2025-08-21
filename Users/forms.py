from django import forms

from .models import Info, User, Favorite, Showed


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Write the Cinema name here...",
                "class": "form-control shadow-sm rounded px-3",
                "title": "Enter the full name of the cinema"
            }),
            "year": forms.NumberInput(attrs={
                "placeholder": "e.g. 2025",
                "class": "form-control shadow-sm rounded text-center",
                "min": 1800,
                "max": 2100,
                "title": "Enter the release year (1800–2100)"
            }),
            "state": forms.TextInput(attrs={
                "placeholder": "e.g. America, Uzbekistan",
                "class": "form-control shadow-sm rounded px-3",
                "title": "Enter the country/state where the cinema was produced"
            }),
            "duration": forms.NumberInput(attrs={
                "placeholder": "Duration in seconds (e.g. 7200)",
                "class": "form-control shadow-sm rounded text-center",
                "min": 1,
                "title": "Enter the duration of the cinema in seconds"
            }),
            "age_limit": forms.NumberInput(attrs={
                "placeholder": "18",
                "class": "form-control shadow-sm rounded text-center",
                "min": 0,
                "max": 30,
                "title": "Enter the age restriction for viewers"
            }),
            "type": forms.Textarea(attrs={
                "placeholder": "Write the type/genre here... (e.g. Premiere, Action, Drama)",
                "class": "form-control shadow-sm rounded px-3",
                "rows": 2,
                "style": "resize:none;",
                "title": "Enter the type or genre of the cinema"
            }),
            "rating": forms.NumberInput(attrs={
                "placeholder": "1 to 10",
                "class": "form-control text-center fw-bold shadow-sm rounded",
                "min": 1,
                "max": 10,
                "step": 1,
                "title": "Enter a rating between 1 and 10"
            }),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Full name (e.g. John Doe)",
                "class": "form-control shadow-sm rounded px-3",
                "title": "Enter the user's full name"
            }),
            "age": forms.NumberInput(attrs={
                "placeholder": "e.g. 25",
                "class": "form-control shadow-sm rounded text-center",
                "min": 1,
                "max": 120,
                "title": "Enter the user's age"
            }),
            "phone_number": forms.TextInput(attrs={
                "placeholder": "+998 90 123 45 67",
                "class": "form-control shadow-sm rounded px-3",
                "title": "Enter the user's phone number"
            }),
            "language": forms.TextInput(attrs={
                "placeholder": "e.g. EN, UZ, RU",
                "class": "form-control shadow-sm rounded text-center",
                "title": "Enter preferred language code"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "example@mail.com",
                "class": "form-control shadow-sm rounded px-3",
                "title": "Enter the user's email address"
            }),
            "password": forms.PasswordInput(attrs={
                "placeholder": "Enter a secure password",
                "class": "form-control shadow-sm rounded px-3",
                "title": "Enter the user's password"
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "title": "Check if the user is active"
            }),
            "is_superuser": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "title": "Check if the user is superuser"
            }),
            "is_staff": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "title": "Check if the user is staff"
            }),
            "is_ban": forms.CheckboxInput(attrs={
                "class": "form-check-input",
                "title": "Check if the user is banned"
            }),
        }


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = "__all__"
        widgets = {
            "rating": forms.NumberInput(attrs={
                "placeholder": "1 to 10",
                "class": "form-control text-center fw-bold shadow-sm rounded",
                "min": 1,
                "max": 10,
                "step": 1,
                "title": "Enter a rating between 1 and 10"
            }),
        }


class ShowedForm(forms.ModelForm):
    class Meta:
        model = Showed
        fields = "__all__"
