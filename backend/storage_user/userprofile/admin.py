from django.contrib import admin

from .models import UserProfile, TestAccount, PremiunAccount

admin.site.register(UserProfile)
admin.site.register(TestAccount)
admin.site.register(PremiunAccount)
