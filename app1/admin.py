from django.contrib import admin
from .models import Post
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
    list_filter = ['created']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,AdminPost)

