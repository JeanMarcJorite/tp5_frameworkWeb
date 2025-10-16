from django import forms
from .models import Book, Review


class BookForm(forms.ModelForm):

    YEAR_CHOICES = [(r, r) for r in range(1984, 2051)]
    year = forms.ChoiceField(choices=YEAR_CHOICES, label='Année de publication')
    
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'year', 'isbn', 'backCover', 'cover']
        labels = {
            'title': 'Titre',
            'publisher': 'Editeur',
            'isbn': 'ISBN',
            'backCover': 'Resumé',
            'cover': 'Image de couverture disponible',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'date', 'rating']
        labels = {
            'content': 'Contenu',
            'date': 'Date',
            'rating': 'Note (sur 5)',
        }
