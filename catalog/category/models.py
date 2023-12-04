from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='название продукта')
    description = models.CharField(max_length=250, verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
