from django.db import models


class UserProfile(models.Model):
    uid = models.CharField(max_length=36)
    days_of_test = models.PositiveIntegerField(max_length=2, default=15)
    days_of_use_as_premiun = models.PositiveIntegerField(max_length=2, default=30)

    def __str__(self) -> str:
        return self.uid


class TestAccount(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    days_for_test = models.DateField(auto_now_add=True)
    has_finish = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "Test Account"


class PremiunAccount(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    day_for_use = models.DateField(auto_now_add=True)
    has_finish = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "Premiun Account"
