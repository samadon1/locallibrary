from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'nums_instances_available': num_instances_available,
    }

    return render(request, 'catalog/index.html', context)

def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }


    return render(request, 'catalog/books.html', context)

def bookDetails(request, pk):
    book = Book.objects.get(id=pk)
    context = {
        'book': book
    }


    return render(request, 'catalog/bookDetails.html', context)

def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }


    return render(request, 'catalog/authors.html', context)

def authorDetails(request, pk):
    author = Author.objects.get(id=pk)

    authorBooks = Book.objects.filter(author = pk)
    
    context = {
        'author': author,
        'books': authorBooks

    }
    return render(request, 'catalog/authorDetails.html', context )