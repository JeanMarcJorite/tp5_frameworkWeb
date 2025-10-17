from django.db import models

class Author(models.Model):
    nom = models.CharField(max_length=35)
    prenom = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.prenom} {self.nom} '
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    backCover = models.TextField()
    cover = models.BooleanField(default=False)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'Le commentaire du {self.date} pour {self.book.title} a une note de {self.rating}/5'


