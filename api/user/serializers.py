from .models import User
from rest_framework import serializers

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "image",
            "created_at",
            "role",
        ]

        extra_kwargs = {
            "role": {"read_only": True},
            "created_at": {"read_only": True}
        }