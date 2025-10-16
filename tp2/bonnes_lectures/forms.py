from django import forms
from .models import Book


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