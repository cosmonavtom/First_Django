# Generated by Django 5.0.9 on 2024-10-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_rename_dogs_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='birth_date'),
        ),
    ]