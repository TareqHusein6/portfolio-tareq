from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    post = models.TextField()
