from django.urls import path, include
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api-v1"

urlpatterns = [
    # registrations
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    # login & Logout with Token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    # Login & logout with JWT
    path("jwt/login/", views.CustomTokenObtainPairView.as_view(), name="jwt-login"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    # Change password
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # Profile
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
    # Verification
    path("verify/", views.SentEmailView.as_view(), name="sent-email"),
    # verify
    path(
        "activation/confrim/<str:token>", views.VerifyViewToken.as_view(), name="verify"
    ),
    # resend verify token
    path(
        "resend/verify/",
        views.ResendVerifyApiView.as_view(),
        name="resend-verification",
    ),
]
