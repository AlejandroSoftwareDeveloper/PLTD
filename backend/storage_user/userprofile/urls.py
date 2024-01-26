from django.urls import path
from .views import (
    UserProfileList,
    UserProfileDetail,
    UserProfileElm,
    TestAccountList,
    TestAccountDetail,
    PremiunAccountList,
    PremiunAccountDetail,
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
    path(
        "userprofile/<int:pk>",
        UserProfileElm.as_view(),
    ),
    path(
        "testaccount/",
        TestAccountList.as_view(),
    ),
    path(
        "testaccount/<int:pk>",
        TestAccountDetail.as_view(),
    ),
    path(
        "premiunaccount/",
        PremiunAccountList.as_view(),
    ),
    path(
        "premiunaccount/<int:pk>",
        PremiunAccountDetail.as_view(),
    ),
]
