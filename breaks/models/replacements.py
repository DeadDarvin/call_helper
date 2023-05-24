from django.contrib.auth import get_user_model
from django.db import models
from .organisations import Organisation

User = get_user_model()


class Replacement(models.Model):
    """ Модель смены, принадлежащей группе """
    group = models.ForeignKey(
        verbose_name='Группа',
        to='breaks.Group',
        on_delete=models.CASCADE,
        related_name='replacements',
    )
    date = models.DateField(
        verbose_name='Дата',
    )
    break_start = models.TimeField(
        verbose_name='Начало обеда',
    )
    break_end = models.TimeField(
        verbose_name='Конец обеда',
    )
    break_max_duration = models.PositiveSmallIntegerField(
        verbose_name='Максимальная продолжительность обеда',
    )

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ['date', ]

    def __str__(self):
        return f'Смена №{self.pk} для {self.group}'


class ReplacementStatus(models.Model):
    """
    Модель статуса сотрудника смены.
    Для просмотра его текущей активности.
    Например: работает/обедает/нет на месте.
    Отображается в модели ReplacementEmployee.
    """
    code = models.CharField(
        verbose_name='Код',
        max_length=16,
        primary_key=True,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=32,
    )
    sort = models.PositiveSmallIntegerField(
        verbose_name='Сортировка',
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='Активность',
        default=True,
    )

    class Meta:
        verbose_name = 'Статус сотрудника смены'
        verbose_name_plural = 'Статусы сотрудников смены'
        ordering = ['sort', ]

    def __str__(self):
        return f'{self.code}:{self.name}'


class ReplacementEmployee(models.Model):
    """
    Модель сотрудника текущей смены.
    Для просмотра его текущей активности.
    Например: работает/обедает/нет на месте.
    """
    employee = models.ForeignKey(
        verbose_name='Имя сотрудника',
        to=User,
        on_delete=models.CASCADE,
        related_name='replacements',
    )
    replacement = models.ForeignKey(
        verbose_name='Смена',
        to='breaks.Replacement',
        on_delete=models.CASCADE,
        related_name='employees',
    )
    status = models.ForeignKey(
        verbose_name='Статус',
        to='breaks.ReplacementStatus',
        on_delete=models.CASCADE,
        related_name='replacement_employees'
    )

    class Meta:
        verbose_name = 'Работник смены'
        verbose_name_plural = 'Работники смены'

    def __str__(self):
        return f'{self.replacement}:{self.employee}'
