from django.db import models
from users.models import NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='breed')
    description = models.CharField(max_length=1000, verbose_name='descriptions')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'breed'
        verbose_name_plural = 'breeds'


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='dog_name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='breed')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='image')
    birth_date = models.DateTimeField(**NULLABLE, verbose_name='birth_date')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'dog'
        verbose_name_plural = 'dogs'
