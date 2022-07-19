from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    text = models.TextField('Text of comment')

    def __str__(self):
        return self.user
