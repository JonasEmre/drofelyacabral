from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.blog_detail, name="blog-detail"),
    path('', views.blog, name="blog"),
]