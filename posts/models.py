from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=255, verbose_name='Titulo')
    post_autor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    post_data = models.DateTimeField(default=timezone.now, verbose_name='Data')
    post_content = models.TextField(verbose_name='Conteudo')
    post_excerpt = models.TextField(verbose_name='Excerto')
    post_category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, null=True,
        verbose_name='Categoria')
    post_img = models.ImageField(
        upload_to='post_img/%Y/%m/%d', blank=True, null=True,
        verbose_name='Imagem')
    post_published = models.BooleanField(
        default=False, verbose_name='Publicado?')

    def __str__(self):
        return self.post_title
