from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import logout

# Create your views here.
# def login(request):
#     return render(request, 'users/login.html')


def register(request):
    if request.user.is_authenticated:
        messages.info(
                request, 'Hesabınız zaten bulunmaktadır.'
            )
        return redirect('ana-sayfa')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"{username} için hesap başarıyla hesap oluşturuldu."
            )
            return redirect("giris")
        else:
            messages.error(request, "Hesap kurulamadı!")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="E-posta adresiniz", max_length=254)


class CustomLoginView(LoginView):
    authentication_form = EmailLoginForm


# class CustomLogoutView(LogoutView):
#     template_name = 'users/logout.html'


def custom_logout(request):
    if request.user.is_authenticated:
        username = str(request.user.username)
        logout(request)
        messages.success(request, f"Güle güle {username}")
    else:
        messages.warning(request, "Zaten oturum açmamıştınız.")
    return redirect("ana-sayfa")
