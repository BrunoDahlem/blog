from django.contrib import admin
from .models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')
    list_display_links = ('id', 'name_category')


admin.site.register(Category, CategoryAdmin)
