from django.contrib import admin

from .models import Comment, Photo, Category


# Register your models here.
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(Category)