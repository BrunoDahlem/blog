from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'post_title', 'post_autor',
                    'post_data', 'post_category', 'post_published')
    list_editable = ('post_published',)
    list_display_links = ('id', 'post_title')
    summernote_fields = ('post_content', 'post_excerpt')


admin.site.register(Post, PostAdmin)
