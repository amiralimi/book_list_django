from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from .models import Book


def main_page(request):
    return render(request, 'book_list/main_page.html')


def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist.")
    return render(request, 'book_list/detail.html', {'book': book})


def view(request):
    book_list = Book.objects.order_by('-book_name')[::-1]
    context = {
        'book_list': book_list,
    }
    return render(request, 'book_list/list.html', context)


def delete(request):
    book_list = Book.objects.order_by('-book_name')[::-1]
    context = {
        'book_list': book_list,
    }
    return render(request, 'book_list/delete.html', context)


def delete_list(request):
    try:
        book_name = request.POST['book']
    except MultiValueDictKeyError:
        return redirect('book_list:list')
    Book.objects.filter(book_name).delete()
    return redirect('book_list:list')
