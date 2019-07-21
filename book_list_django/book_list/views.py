from django.shortcuts import render, redirect
from django.http import Http404
from django.utils.datastructures import MultiValueDictKeyError
from .models import Book
import datetime


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


def add(request):
    return render(request, 'book_list/add.html')


def add_book(request):
    try:
        book_name = request.POST['book_name']
        pub_date = request.POST['pub_date']
        page_num = request.POST['page_num']
        if book_name == "" or pub_date == "" or page_num == "":
            raise Exception("no entered value")
        first_print = request.POST['first_print']
    except MultiValueDictKeyError:
        first_print = False
    except Exception:
        context = {
            'error_message': 'please fill all the boxes'
        }
        return render(request, 'book_list/add.html', context)
    pub_date = datetime.datetime.strptime(pub_date, '%Y-%m-%d').date()
    page_num = int(page_num)
    b = Book(book_name=book_name, pub_date=pub_date, page_num=page_num, first_print=first_print)
    b.save()
    return redirect('book_list:list')


def edit_list(request):
    book_list = Book.objects.order_by('-book_name')[::-1]
    context = {
        'book_list': book_list,
    }
    return render(request, 'book_list/edit_list.html', context)


def edit(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'id': book.id,
        'book_name': book.book_name,
        'pub_date': book.pub_date.strftime("%Y-%m-%d"),
        'page_num': book.page_num,
        'first_print': book.first_print,
    }
    return render(request, 'book_list/edit.html', context)


def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    try:
        book_name = request.POST['book_name']
        pub_date = request.POST['pub_date']
        page_num = request.POST['page_num']
        if book_name == "" or pub_date == "" or page_num == "":
            raise Exception("no entered value")
        first_print = request.POST['first_print']
    except MultiValueDictKeyError:
        first_print = False
    except Exception:
        context = {
            'error_message': 'please fill all the boxes',
            'id': book.id,
            'book_name': book.book_name,
            'pub_date': book.pub_date.strftime("%Y-%m-%d"),
            'page_num': book.page_num,
            'first_print': book.first_print,
        }
        return render(request, 'book_list/edit.html', context)
    pub_date = datetime.datetime.strptime(pub_date, '%Y-%m-%d').date()
    page_num = int(page_num)
    b = Book.objects.get(pk=book_id)
    b.book_name = book_name
    b.pub_date = pub_date
    b.page_num = page_num
    b.first_print = first_print
    b.save()
    return redirect('book_list:list')
