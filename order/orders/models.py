from django.db import models


class Order(models.Model):
    description = models.TextField('Описание', default='', blank=True)
    is_ready = models.BooleanField('Готовность', default=False, db_index=True)

    def __str__(self):
        return 'Order {}'.format(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

