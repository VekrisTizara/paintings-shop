from django.contrib.auth.models import User, AbstractUser

from django.db import models

class MyUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
