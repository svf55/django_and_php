from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class Invoice(models.Model):
    number = models.CharField('Номер', max_length=256, unique=True, db_index=True)
    orders = JSONField()
    created_at = models.DateTimeField('Создана', default=timezone.now)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Накладная'
        verbose_name_plural = 'Накладные'

