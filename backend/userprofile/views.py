from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import UserProfile
from .serializers import UserProfileSerializer

class UserProfileList(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

