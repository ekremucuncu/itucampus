from django.contrib import admin
from .models import Question,Answer

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','created_on','author')
    search_fields = ['title', 'created_on','author']
    prepopulated_fields = {'slug': ('title',)}

class AnswerAdmin(admin.ModelAdmin):
    list_display=('created_on','author',"pk")
    search_fields=['created_on','author']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
