from rest_framework import serializers
from .models import UserProfile, TestAccount, PremiunAccount


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class TestAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAccount
        fields = "__all__"


class PremiunAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiunAccount
        fields = "__all__"
