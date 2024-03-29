from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']
    list_filter = ['created', 'status']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,AdminPost)
admin.site.register(Comment)

