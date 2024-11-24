"""
Views for the User API.
"""

from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user"""

    serializer_class = UserSerializer
