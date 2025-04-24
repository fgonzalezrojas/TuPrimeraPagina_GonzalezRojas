from django.urls import path
from .views import UserRegisterView, UserLoginView, logout_view , UserChangeView, AvatarUpdateView

app_name = "cuentas"

urlpatterns = [
    path("", UserLoginView.as_view(), name= "login"),
    path("signup/", UserRegisterView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    # AVATAR
    path("editar/", UserChangeView.as_view(), name="editar"),  
    path("subir_avatar/", AvatarUpdateView.as_view(), name="subir_avatar")
    ]
