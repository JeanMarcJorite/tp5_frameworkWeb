from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .models import Book, Review
from .forms import BookForm, ReviewForm

# Create your views here.
def about(request):
    return render(request, 'about.html')


def welcome(request): 
    return render(request, 'welcome.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.reviews.order_by('-date')
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews})

def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'new_book.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return redirect('book_list')

def modify_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'modify_book.html', {'form': form, 'book': book, "button_label": "Modifier"})


def new_review(request,id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_detail', id=book.id)
    else:
            form = ReviewForm(initial={'date': datetime.date.today()})

    return render(request, 'new_review.html', {"form": form, 'book': book})
   
   