from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    post = models.TextField(max_length=64, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='post_author',blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.post)
        super().save(*args, **kwargs)


    def __repr__(self):
        return f"{self.post}"

    def __str__(self):
        return self.post


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_comment')
    comment=models.TextField(max_length=256)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='post_comment_author',blank=True,null=True)
    author_security=models.ForeignKey(User, on_delete= models.CASCADE,related_name='post_comment_author_security')
    created_on = models.DateTimeField(auto_now_add=True)
    anonn=models.BooleanField()

    class Meta:
        ordering = ['-created_on']


    def get_absolute_url(self):
        return reverse("comment_detail",kwargs={'pk':self.pk})


    def __repr__(self):
        return f"{self.comment}"

    def __str__(self):
        return self.comment
