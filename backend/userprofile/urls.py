from django.urls import path
from .views import (
    UserProfileList,
    UserProfileDetail,
   
)


urlpatterns = [
    path(
        "userprofile/",
        UserProfileList.as_view(),
    ),
    path(
        "userprofile/<int:pk>",
        UserProfileDetail.as_view(),
    ),
   
]
