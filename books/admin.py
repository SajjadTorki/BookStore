from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'user', 'book', 'datetime_created']


# For register ti admin we can use the upper Syntax
admin.site.register(Book)
admin.site.register(Comment, CommentAdmin)
