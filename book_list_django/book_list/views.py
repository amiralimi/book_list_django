from django.shortcuts import render
from django.http import Http404
from .models import Book


def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist.")
    return render(request, 'book_list/detail.html', {'book' : book})


def view(request):
    book_list = Book.objects.order_by('-book_name')
    context = {
        'book_list': book_list,
    }
    return render(request, 'book_list/list.html', context)
