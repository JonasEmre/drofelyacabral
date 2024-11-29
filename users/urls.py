from django.urls import path
from . import views

urlpatterns = [
    path('giris/', views.login, name="giris"),
    path('cikis/', views.CustomLogoutView, name='cikis'),
    path('kayit-ol/', views.register, name="kayit-ol"),
]