# Generated by Django 4.0.6 on 2022-07-26 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name_category',
            field=models.CharField(max_length=255, verbose_name='Nome da Categoria'),
        ),
    ]
