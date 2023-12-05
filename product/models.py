from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='название продукта')
    description = models.CharField(max_length=250, verbose_name='описание')
    photo_preview = models.ImageField(**NULLABLE, upload_to='preview/', verbose_name='изображение (превью)')
    category = models.CharField(max_length=100, verbose_name='категория')
    piece_price = models.BooleanField(verbose_name='цена за штуку')
    creation_date = models.DateField(verbose_name='дата создания')
    update_date = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
