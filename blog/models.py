from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    post = models.TextField()

    # returns the real title of the project in admin's page
    def __str__(self):
        return self.title
