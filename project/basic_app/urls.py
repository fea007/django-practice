from django.urls import path
from basic_app import views

app_name = "basic_app"
urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'register/', views.register, name="register"),
    path(r'login/', views.user_login, name="login"),
    path(r'logout/', views.user_logout, name="logout")
]
