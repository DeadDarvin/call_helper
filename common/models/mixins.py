from django.db import models


class BaseDictModelMixin(models.Model):
    """
    Абстрактная модель для отображения
    статусов. Например, статуса сотрудника
    или статуса обеда.
    """
    code = models.CharField(
        verbose_name='Код',
        max_length=16,
        primary_key=True,
    )
    name = models.CharField(
        verbose_name='Название статуса',
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
        abstract = True
        ordering = ['sort', ]

    def __str__(self):
        return f'{self.code}:{self.name}'
