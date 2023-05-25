from django.contrib.auth import get_user_model
from django.db import models

from .dicts import BreakStatus
from ..constans import BREAK_CREATED_STATUS, BREAK_CREATED_DEFAULT

User = get_user_model()


class Break(models.Model):
    """
    Модель обеда.
    Для бронирования времени сотрудником.
    Для подтверждения времени менеджером.
    """
    replacement = models.ForeignKey(
        verbose_name='Смена',
        to='breaks.Replacement',
        on_delete=models.CASCADE,
        related_name='breaks',
    )
    employee = models.ForeignKey(
        verbose_name='Сотрудник',
        to=User,
        on_delete=models.CASCADE,
        related_name='breaks',
    )
    break_start = models.TimeField(
        verbose_name='Начало обеда',
        blank=True,
        null=True,
    )
    break_end = models.TimeField(
        verbose_name='Конец обеда',
        blank=True,
        null=True,
    )
    status = models.ForeignKey(
        verbose_name='Статус',
        to='breaks.BreakStatus',
        on_delete=models.RESTRICT,
        related_name='breaks',
        blank=True,
    )

    class Meta:
        verbose_name = 'Обеденный перерыв'
        verbose_name_plural = 'Обеденные перерывы'
        ordering = ['-replacement__date', 'break_start', ]

    def __str__(self):
        return f'Обед сотрудника {self.employee}:{self.status}'

    def save(self, *args, **kwargs):
        if not self.pk:
            status, created = BreakStatus.objects.get_or_create(
                code=BREAK_CREATED_STATUS,
                defaults=BREAK_CREATED_DEFAULT
            )
            self.status = status
            # self.status = BreakStatus.objects.filter(code=BREAK_CREATED_STATUS).first()
        return super().save(*args, **kwargs)
