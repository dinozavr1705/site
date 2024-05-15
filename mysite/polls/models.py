from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    rating = models.FloatField(max_length=3, default=0)
    skills = models.CharField(max_length=1000, default="Отсутствуют")
    tg = models.CharField(max_length= 200,default="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    github = models.CharField(max_length= 200, default = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")