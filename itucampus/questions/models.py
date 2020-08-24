from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='question_author')
    question=models.ImageField(upload_to='question/',blank=True,name="question")
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=20, unique=True)
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='answer_author')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='question_answer')
    answer=models.ImageField(upload_to='question/',blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=400)

    class Meta:
        ordering = ['-created_on']


    def get_absolute_url(self):
        return reverse("comment_detail",kwargs={'pk':self.pk})
