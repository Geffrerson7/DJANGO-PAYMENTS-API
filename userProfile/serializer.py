from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "photo",
            "username",
            "id",
        )
        read_only_fields = ("username",)
