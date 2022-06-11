from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, firstName, lastName, email, password=None):
        if firstName is None:
            raise TypeError('Users should have first Name')
        if lastName is None:
            raise TypeError('Users should have Last Name')
        if email is None:
            raise TypeError('Users should have email')
        user = self.model(firstName=firstName, lastName=lastName, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, firstName, lastName, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(firstName, lastName, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    profile_image = models.ImageField(upload_to='uploads/profileImages', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # set one time date as created date
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  # Set email as default login instead of username
    REQUIRED_FIELDS = ['firstName', 'lastName']
    objects = UserManager()

    def __str__(self):
        return self.email

    def Access_token(self):
        refresh = RefreshToken.for_user(self)
        myDict = {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
        return myDict

    def Refresh_token(self):
        refresh = RefreshToken.for_user(self)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        myDict = {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
        return myDict

