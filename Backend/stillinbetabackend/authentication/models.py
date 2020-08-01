from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users Must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        # Not necessary to write anything inside brackets
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)

    # Custom Manager To handle users with email field as the main field
    # instead of username
    objects = UserProfileManager()
    # Done to handle Django Admin
    USERNAME_FIELD = 'email'
    # Required Field can include more fields
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve Full Name"""
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """Return String representation of user"""
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}
