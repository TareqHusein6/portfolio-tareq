from django.db import models
#models.py used for database models (class of rows)


class Project(models.Model):
    title = models.CharField(max_length=100)
    disc = models.CharField(max_length=250)
    image = models.ImageField('portfolio/images/')#uses pillow module
    url = models.URLField(blank=True) #if blank=true then it means that URLfield can be empty in the database(default is false)