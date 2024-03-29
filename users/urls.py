# users/urls.py

from django.urls import path
from .views import *

app_name = 'users'
urlpatterns = [
    # path('', home, name="home"),
    # path("signup/", SignUp.as_view(), name="signup"),
    path("signup/", UserRegister, name="signup"),
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_user_profile/', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('update_user_profile/<int:pk>/', UpdateProfilePageView.as_view(), name='update_user_profile'),
]
