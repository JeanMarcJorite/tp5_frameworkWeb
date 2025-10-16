from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    backCover = models.TextField()
    cover = models.BooleanField(default=False)

    def __str__(self):
        return self.title