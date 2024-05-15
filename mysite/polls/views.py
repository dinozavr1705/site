import random
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import json
import sqlite3
from sqlite3 import *
from django.contrib.auth.urls import *
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm, CustomAuthForm
from .models import User
import hashlib

def number_of_users(request):
    a = User.objects.all
    b = []
    for i in a:
        b.append(i)


def profile(request):
    current_user = request.user
    skills1 = current_user.skills
    skills = ""
    skills1 = skills1.replace("'", "")
    skills1 = skills1.replace("[", "")
    skills1 = skills1.replace("]", "")
    skills1 = skills1.split(",")
    for i in skills1:
        skills += f"{i}, "
    skills = list(skills)
    skills.pop(len(skills) - 2)
    skills2 = ""
    for i in skills:
        skills2 += f"{i}"
    print(skills2)
    return render(request, 'main/my_profile.html', {"skills": skills2, "rating": current_user.rating})


def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    skills1 = user.skills
    skills = skills1.split(",")

    return render(request, "main/profile.html", {"user1": user, "skills": skills})


def find_user(request):
    if request.method == "POST":
        user = User(username=request.POST.get("username"))
        users = [user.skills]
        print(users)
        return render(request, "main/user_list.html", {"users": users})
    return render(request, "main/find.html")

def sort_users(request):
    all_users = User.objects.all()
    if request.method == "POST":
        if request.POST.get("Subject") == "юзернейм":
            cryteries = request.POST.get("cryteries").lower()
            users = [User.objects.get(username=cryteries)]
            print(users)
            return render(request, "main/user_list.html", {"users": users})
        else:
            cryteries = request.POST.get("cryteries").lower()
            users = []
            for user in all_users:
                a = ["[", "]", "'"]
                new_skills = user.skills
                for char in a:
                    new_skills = new_skills.replace(char, "")
                print(new_skills)
                for i in new_skills.split(","):
                    if i == cryteries:
                        users.append(user)
            print(users)
            return render(request, "main/user_list.html", {"users": users})
    return render(request, "main/sort.html")


def user_login(request):
    if request.method == "POST":
        form = CustomAuthForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(username = username)
        print("DA")
        if user is not None and check_password(password, user.password):
                  login(request, user)
                  return redirect("/")
                  print("DA")
        else:
            return render(request, "main/registration/login.html", {"form": CustomAuthForm})
    else:
        return render(request, "main/registration/login.html", {"form": CustomAuthForm})


def func(request):
    return render(request, 'main/registration.html')


def password_change(request):
    user = request.user
    password = user.password
    if request.method == "POST":
        print(password)
        print(request.POST.get("current_password"))
        if check_password(request.POST.get("current_password"), password):
            new_password = request.POST.get("new_password")
            user.set_password(new_password)
            print(".")
            user.save()
            login(request, user)
            return redirect("/")
    return render(request, "main/password_change.html")


def password_change2(request):
    user = request.user
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        user.set_password(new_password)
        print(".")
        user.save()
        login(request, user)
        return redirect("/")
    return render(request, "main/password_change2.html")


def username_change(request):
    user = request.user
    if request.method == "POST":
        print(".")
        new_username = request.POST.get("new_username")
        user.username = new_username
        user.save()
        return redirect("/polls/profile")
    return render(request, "main/username_change.html")


def skills_change(request):
    user = request.user
    if request.method == "POST":
        user.skills = request.POST.get("new_skills")
        user.save()
        print("DA")
    return render(request, "main/skills_change.html")

def random_user(request):
    if request.method == "POST":
        users = User.objects.all()
        a = []
        for i in users:
            a.append(i)
        user = a[random.randint(0,len(a) - 1)]
        return render(request,"main/profile.html",{"user1":user})
    return render(request,"main/random_user.html")

def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('username')
            password = request.POST.get('password')
            github = request.POST.get('github')
            tg = request.POST.get('tg')
            again_password = request.POST.get("again_password")
            user = User.objects.filter(username = name).exists()
            if user == False:
                if password == again_password:
                    newuser = User.objects.create(username=name, password=password, rating=0, github=github,
                                              tg="https://t.me/" + tg)
                    newuser.set_password(password)
                    print(".")
                    newuser.save()
                    login(request, newuser)
                    return redirect("/")
                else:
                    return render(request, 'main/registration/registration.html',{'form': form, "error": "пароль не соответствует"})
            else:
                return render(request, 'main/registration/registration.html', {'form': form,"error":"такой пользователь уже существует"})

    else:
        form = UserForm()
    return render(request, 'main/registration/registration.html', {'form': form})


def list_of_profiles(request):
    a = QuerySet.iterator

    print(a)
    return render(request, "main/page_of_profiles.html", {"a": a})


def user_list(request):
    all_users = User.objects.all()
    for i in all_users:
        print(i.username)
        print(i.skills)

    return render(request, "main/user_list.html", {"users": all_users})


def signout(request):
    print("Da")
    logout(request)
    print("Da")
    return HttpResponseRedirect('/')


def test_func(request):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    rows = cursor.fetchall()
    a = ""


def loginTest(request):
    return render(request, "main/registration/login.html")
