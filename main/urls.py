from . import views
from .views import CustomLoginView,CustomLogoutView
from django.urls import path

app_name="auth"

urlpatterns = [
    path("",views.index,name="index"),
    path("login/",CustomLoginView.as_view(),name="login"),
    path("logout/",CustomLogoutView.as_view(),name="logout"),
    path("register/",views.register_view,name="register"),
]