from django.db import models

# Create your models here.


class Category(models.Model):
    name_category = models.CharField(
        max_length=255, verbose_name='Nome da Categoria')

    def __str__(self):
        return self.name_category
