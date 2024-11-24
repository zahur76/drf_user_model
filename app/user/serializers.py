"""
Serializers for the user API View
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user objects"""

    password2 = serializers.CharField(min_length=5, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "password2", "username"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with validated data"""
        validated_data.pop("password2")
        print(
            validated_data.get(
                "email",
            )
        )

        return get_user_model().objects.create_user(**validated_data)

    def validate_email(self, value):
        """Validate email length"""

        if len(value) > 50:
            raise serializers.ValidationError("Email too long")
        return value

    def validate(self, data):
        """
        Ensure passwords match before saving user
        """
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError("Passwords do not match!")

        return data
