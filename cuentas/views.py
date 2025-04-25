from django.shortcuts import render

# Create your views here.

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView , UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return redirect("cuentas:login")
    
class UserRegisterView(CreateView):
    template_name = "cuentas/00 signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("cuentas:login")
class UserLoginView(LoginView):
    template_name = "cuentas/01 login.html"
    
# AVATAR

from .models import Avatar
from .forms import CustomUserForm, AvatarForm
from django.shortcuts import render
from django.views import View
class UserChangeView(LoginRequiredMixin, View):
    def get(self, request):
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        user_form = CustomUserForm(instance=request.user)
        avatar_form = AvatarForm(instance=avatar)
        return render(request, 'cuentas/02 editar perfil.html', {
            'user_form': user_form,
            'avatar_form': avatar_form,
        })

    def post(self, request):
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        user_form = CustomUserForm(request.POST, instance=request.user)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar_form.save()
            return redirect('vinoteca:home')
        return render(request, 'cuentas/02 editar perfil.html', {
            'user_form': user_form,
            'avatar_form': avatar_form,
        })
class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'cuentas/03 subir avatar.html'
    success_url = reverse_lazy('vinoteca:home')

    def get_object(self, queryset=None):
        avatar, _ = Avatar.objects.get_or_create(user=self.request.user)
        return avatar

