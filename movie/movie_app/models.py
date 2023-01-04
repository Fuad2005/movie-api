from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(max_length=200)


    def __str__(self):
        return self.title
