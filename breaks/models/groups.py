from django.contrib.auth import get_user_model
from django.db import models
from .organisations import Organisation

User = get_user_model()


class Group(models.Model):
    """ Модель группы, принадлежащей организации """
    organisation = models.ForeignKey(
        verbose_name='Принадлежит организации',
        to='breaks.Organisation',
        on_delete=models.CASCADE,
        related_name='groups',
    )
    name = models.CharField(
        verbose_name='Название группы',
        max_length=200,
    )
    manager = models.ForeignKey(
        verbose_name='Менеджер группы',
        to=User,
        on_delete=models.RESTRICT,
        related_name='group_managers',
    )
    employees = models.ManyToManyField(
        verbose_name='Сотрудники группы',
        to=User,
        related_name='groups_employees',
        blank=True,
    )
    min_active = models.PositiveSmallIntegerField(
        verbose_name='Минимальное количество активных сотрудников',
        null=True,
        blank=True,
    )
    break_start = models.TimeField(
        verbose_name='Стандартное время начала обеда',
        null=True,
        blank=True,
    )
    break_end = models.TimeField(
        verbose_name='Стандартное время окончания обеда',
        null=True,
        blank=True,
    )
    break_max_duration = models.PositiveSmallIntegerField(
        verbose_name='Максимальная длительность обеда (мин)',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name', ]

    def __str__(self):
        return self.name
