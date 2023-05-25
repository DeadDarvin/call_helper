from django.contrib.auth import get_user_model
from common.models.mixins import BaseDictModelMixin


class ReplacementStatus(BaseDictModelMixin):
    """
    Модель статуса сотрудника смены.
    Для просмотра его текущей активности.
    Например: работает/обедает/нет на месте.
    Отображается в модели ReplacementEmployee.
    """
    class Meta:
        verbose_name = 'Статус сотрудника смены'
        verbose_name_plural = 'Статусы сотрудников смены'


class BreakStatus(BaseDictModelMixin):
    """
    Модель статуса обеда.
    """
    class Meta:
        verbose_name = 'Статус обеда'
        verbose_name_plural = 'Статусы обедов'
