from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name="Пользователь",
        primary_key=True
    )
    telegram_id = models.CharField(max_length=20, verbose_name="TG ID")

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
