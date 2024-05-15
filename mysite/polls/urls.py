from django.urls import path
from django.contrib.auth import views as auth_views, logout
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .forms import CustomAuthForm
from .views import *

urlpatterns = [
    path("registration/", new_user, name="registration"),
    #path(path('login',  auth_views.LoginView.as_view(template_name='main/registration/login.html', authentication_form=CustomAuthForm),
         #name='login')),
    path('user/<int:user_id>/', user_profile, name='user_profile'),
    path("profile/",profile, name = "profile"),
    path("profiles/",list_of_profiles,name = "list_of_profiles"),
    path("list_of_all_users/",user_list, name = "userlist"),
    path("my_profile/",profile,name = "vjq ghjabkm"),
    path("change_password/",password_change, name = "password_change"),
    path("change_password2/",password_change2,name = "password_change2"),
    path("change_username/",username_change,name = "username_change"),
    path("change_skills/",skills_change, name = "skills_change"),
    path("login/",user_login,name ="user_login"),
    path("signout/",signout,name = "signout"),
    path("random_user/",random_user,name = "random_user"),
    path("registration/",new_user, name = "registration"),
    path("sort/",sort_users,name = "sort")
]


