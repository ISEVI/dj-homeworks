from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    #date = request.GET
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def books_pub_date(request, date):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=date)
    next_date = Book.objects.filter(pub_date__gt=date).first()
    previous_date = Book.objects.filter(pub_date__lt=date).first()
    context = {
        'books': books,
        'next_date': next_date,
        'previous_date': previous_date,
        'date': date
    }
    return render(request, template, context)
