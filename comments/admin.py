from django.contrib import admin

from .models import Comments

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_autor', 'comment_name',
                    'comment_post', 'comment_date', 'comment_published')
    list_display_links = ('id', 'comment_autor', 'comment_name')
    list_editable = ('comment_published',)


admin.site.register(Comments, CommentAdmin)
