# Generated by Django 3.2.3 on 2021-06-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('idConcepto', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombreConcepto', models.CharField(max_length=50, verbose_name='Concepto')),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('idObra', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreObra', models.CharField(max_length=50, verbose_name='Obra')),
                ('nombreArtista', models.CharField(max_length=6, verbose_name='Artista')),
            ],
        ),
    ]