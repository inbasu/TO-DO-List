from django.urls import path, include

from users.views import CustomLoginView, UserCreateView, UserLogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("registration/", UserCreateView.as_view(), name="registartion"),
]
