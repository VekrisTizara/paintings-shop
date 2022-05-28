from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    email = models.EmailField('email address', unique=True)

