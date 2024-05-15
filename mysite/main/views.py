from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse


def button_view(request):
    return render(request, 'main/registration.html')


def test_function(request):
    return render(request, "main/index.html")


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        if not form.is_valid():
            return render(request, 'main/registration/login.html',
                          {"form": AuthenticationForm(),
                           "error": "Невалидные данные"})
    else:
        return render(request, "main/registration/login.html", {'form': form, 'error': ""})

