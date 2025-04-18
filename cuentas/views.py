from django.shortcuts import render

# Create your views here.

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect("cuentas:login")
    
class UserRegisterView(CreateView):
    template_name = "cuentas/00 signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("cuentas:login")
class UserLoginView(LoginView):
    template_name = "cuentas/01 login.html"
    success_url = reverse_lazy("vinoteca:home")

    def get_success_url(self):  # Agrega este método
        return self.success_url
    


