from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, logout
from django.views.generic import CreateView

from users.forms import UserRegestrationForm

# Create your views here.

User = get_user_model()


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "users/templates/login.html"
    success_url = "home"


class UserCreateView(CreateView):
    model = User
    form_class = UserRegestrationForm
    template_name = "users/templates/registration.html"
    success_url = "home"


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")
