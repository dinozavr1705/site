from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, PasswordInput

from .models import User


class UserForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={'id':'user','placeholder': 'Логин'}), label='')
    password = forms.CharField(widget=PasswordInput(attrs={'id':'pass', 'placeholder':'Пароль'}), label = '')
    github = forms.CharField(widget=TextInput(attrs={'id':'github','placeholder': 'ссылка на гитхаб'}), label='')
    tg = forms.CharField(widget=TextInput(attrs={'id':'tg','placeholder': 'ссылка на тг'}), label='')
    class Meta:
        model = User

    fields = '__all__'

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'id':"username",'class':'validate','placeholder': 'Логин'}), label='')
    password = forms.CharField(widget=PasswordInput(attrs=({'id':"password",'placeholder':'Пароль'})), label='')