# Generated by Django 4.0.6 on 2022-07-26 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0002_alter_category_name_category'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(verbose_name='Conteudo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_excerpt',
            field=models.TextField(verbose_name='Excerto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_published',
            field=models.BooleanField(default=False, verbose_name='Publicado?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
    ]
