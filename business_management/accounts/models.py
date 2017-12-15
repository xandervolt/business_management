from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password=None):
        
        if not email:
            raise ValueError("You must enter an email address")
            
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            first_name,
            last_name,
            email,
            username,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=80, unique=True)
    bio = models.CharField(max_length=255, blank=True, default="")
    title = models.CharField(max_length=100, blank=True, default="")
    prof_image = models.ImageField(blank=True, null=True, upload_to='business_management/static/images/users/avatars')
    digital_sig = models.ImageField(blank=True, null=True, upload_to='business_management/static/images/users/signatures')
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    email_confirmed = models.BooleanField(default=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    def get_long_name(self):
        return"{} (@{})".format(self.first_name, self.last_name)