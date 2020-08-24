from django.contrib import admin
from .models import Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('post', 'slug','created_on','author')
    search_fields = ['post', 'created_on','author']
    prepopulated_fields = {'slug': ('post',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=('comment','created_on','author',"pk")
    search_fields=['comment','created_on','author']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
