from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_id', 'full_name', 'age', 'phone_number', 'language', 'email', 'password', 'created_time',
                  'is_active', 'is_superuser', 'is_staff', 'is_ban',)

