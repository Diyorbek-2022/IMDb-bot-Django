from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    year = models.IntegerField()  # IntegerField da max_length ishlatilmaydi
    state = models.CharField(max_length=50)
    duration = models.IntegerField()
    age_limit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])

    def __str__(self):
        return f"{self.name} ({self.year})"


class Cinema(models.Model):
    id = models.AutoField(primary_key=True)
    cinema_url = models.TextField()
    info = models.OneToOneField(Info, on_delete=models.CASCADE, related_name="cinema", null=True, blank=True)
    cinema_code = models.TextField(unique=True)
    added_time = models.DateTimeField(auto_now_add=True)
    next = models.IntegerField(null=True, blank=True)
    previous = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.info.name if self.info else "No info"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    language = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    created_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_ban = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name="favorites")
    added_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        if self.cinema.info:
            return f"{self.user.full_name} - Favorite {self.cinema.info.name}"
        return f"{self.user.full_name} - Favorite (No info)"


class Showed(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="showed")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name="showed")
    showed_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.cinema.info:
            return f"{self.user.full_name} - Showed {self.cinema.info.name}"
        return f"{self.user.full_name} - Showed (No info)"
