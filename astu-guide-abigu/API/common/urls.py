from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.RegisterAPIView.as_view()),
    path("login", views.LoginAPIView.as_view()), #
    path("user/", views.UserAPIView.as_view()), #
    path("logout/", views.LogoutAPIView.as_view()), #
    path("account/info/", views.ProfileInfoAPIView.as_view()), #
    path("account/password/", views.ProfilePasswordAPIView.as_view()), #
]