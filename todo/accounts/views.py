from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserRegister


# Create your views here.
def register(request):
    try:
        form = CustomUserRegister()

        if request.method == "POST":
            form = CustomUserRegister(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Registeration successfully")
                return redirect('login')
        context = {"form": form}

        return render(request, 'accounts/register.html', context)
    except:
        pass


def loginpage(request):

    try:
        if request.user.is_authenticated:
            messages.error(request, "You are already loged in")
            return redirect('home')
        else:
            if request.method == "POST":
                lusername = request.POST.get('username')
                lpassword = request.POST.get('password')

                user = authenticate(
                    request, username=lusername, password=lpassword)
                if user is not None:
                    login(request, user)
                    messages.success(request, "loged in successfully")
                    return redirect('home')

            return render(request, 'accounts/login.html')
    except:
        pass


def logoutpage(request):
    try:
        logout(request)
        return redirect('login')
    except:
        pass
