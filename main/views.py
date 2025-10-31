from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth import login


# Create your views here.


def index(request):
    return render(request,"main/index.html")


class CustomLoginView(LoginView):
    template_name = "main/login.html"
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = "auth:login"



def register_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"account created, you can login now!")
            return redirect("auth:login")
    else:
        form=UserCreationForm()
    return render(request,"main/register.html",{"form":form})