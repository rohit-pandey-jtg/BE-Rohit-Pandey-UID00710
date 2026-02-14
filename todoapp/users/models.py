from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """
    Add manager methods here to create user and super user
    """



class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Needed fields
    - password (already inherited from AbstractBaseUser; encrypt password before saving to database)
    - last_login (already inherited from AbstractBaseUser)
    - is_superuser
    - first_name (max_length=30)
    - email (should be unique)
    - is_staff
    - date_joined (default should be time of object creation)
    - last_name (max_length=150)
    """
    is_superuser = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)
    USERNAME_FIELD = 'email'
    objects = UserManager()

