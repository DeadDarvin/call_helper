from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from ..managers import CustomUserManager
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Эл. Почта",
        unique=True,
        null=False,
        blank=False
    )
    username = models.CharField(
        verbose_name="Имя пользователя",
        max_length=255,
        null=True,
        blank=True
    )
    phone_number = PhoneNumberField(
        verbose_name="Номер телефона",
        unique=True,
        null=True,
        blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", ]
    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

