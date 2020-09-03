from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        #Normalizovanje email-a (postavljamo prvi deo email-a malim slovima)
        email = self.normalize_email(email)
        #Kreiramo novog user-a. .model se odnosi na model koji koristi UserProfileManager klasu
        user = self.model(email=email, name=name)
        #Hesiranje password field-a
        user.set_password(password)
        #Standardna konvencija kako se cuvaju objekti, iako koristimo samo jednu bazu,
        #Konfencija nalaze da se uvek doda atribut u kojoj bazi cuvamo objekat
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #USERNAME_FIELD overraduje defaultino prijavljivanje, tj. koriscenje email-a umesto username-a
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive ful name of user"""
        return self.name

    def get_shor_name(self):
        """Retrive short name of user"""
        return self.name

    def __str__(self):
        """Return string reprezentation of UserProfile"""
        return self.email + ' ' + self.name
