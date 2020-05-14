from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):
    """manager for userprofile to specify some functions"""

    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("User must have email")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db) #saving object in django

        return user


    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database model for userin the system """

    email=models.EmailField(max_length=120,unique=True)
    name=models.CharField(max_length=120)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    objects=UserProfileManager()


    def get_FullName(self):
        """Retreive full name"""
        return self.name

    def short_name(self):
        return self.name

    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    """ profile status update"""
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """ return model as a string """
        return self.status_text
