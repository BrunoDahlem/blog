from django.db import models
from django.contrib.auth.models import User

from posts.models import Post
from django.utils import timezone

# Create your models here.


class Comments(models.Model):
    comment_name = models.CharField(max_length=255, verbose_name='Nome')
    comment_email = models.EmailField(verbose_name='E-mail')
    comment_autor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    comment_description = models.TextField(verbose_name='Comentário')
    comment_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name='Post')
    comment_date = models.DateTimeField(
        default=timezone.now, verbose_name='Data')
    comment_published = models.BooleanField(
        default=False, verbose_name='Publicado?')

    def __str__(self):
        return self.comment_name
