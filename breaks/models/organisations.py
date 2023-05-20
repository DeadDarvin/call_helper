from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Organisation(models.Model):
    """ Модель организации. Ей принадлежат группы """
    name = models.CharField(
        verbose_name='Название организации',
        max_length=200,
    )
    director = models.ForeignKey(
        verbose_name='Директор организации',
        to=User,
        on_delete=models.RESTRICT,
        related_name='organisation_directors',
    )
    employees = models.ManyToManyField(
        verbose_name='Сотрудники организации',
        to=User,
        related_name='organisation_employees',
        blank=True,
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name', ]

    def __str__(self):
        return self.name
