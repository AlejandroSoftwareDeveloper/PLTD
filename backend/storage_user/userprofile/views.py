from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import UserProfile, TestAccount, PremiunAccount
from .serializers import (
    UserProfileSerializer,
    TestAccountSerializer,
    PremiunAccountSerializer,
)


class UserProfileList(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    # def get_queryset(self):
    #     queryset = UserProfile.objects.all()
    #     idelm = self.request.query_params.get("myid")
    #     if idelm is not None:
    #         queryset = queryset.filter(pk=idelm)
    #     return queryset


class UserProfileElm(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["uid"]


class TestAccountList(generics.ListCreateAPIView):
    serializer_class = TestAccountSerializer

    def get_queryset(self):
        queryset = TestAccount.objects.all()
        userprofile = self.request.query_params.get("userprofile")
        if userprofile is not None:
            queryset = queryset.filter(user_profile=userprofile)
        return queryset


class TestAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestAccountSerializer
    queryset = TestAccount.objects.all()


class PremiunAccountList(generics.ListCreateAPIView):
    serializer_class = PremiunAccountSerializer

    def get_queryset(self):
        queryset = PremiunAccount.objects.all()
        userprofile = self.request.query_params.get("userprofile")
        if userprofile is not None:
            queryset = queryset.filter(user_profile=userprofile)
        return queryset


class PremiunAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PremiunAccountSerializer
    queryset = PremiunAccount.objects.all()
