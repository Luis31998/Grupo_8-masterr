# Generated by Django 3.2.3 on 2021-06-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210622_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='nombreAsuntos',
            field=models.CharField(max_length=50, verbose_name='Asunto'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombreMensaje',
            field=models.CharField(max_length=50, verbose_name='Mensaje'),
        ),
    ]
