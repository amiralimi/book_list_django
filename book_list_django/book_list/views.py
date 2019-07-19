from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def detail(request, book_id):
    return HttpResponse(f"You're looking at book: {Book.objects.get(pk=book_id)}")


def view_list(request):
    output = ""
    for i, b in enumerate(Book.objects.order_by('-book_name')):
        output += f"{i+1}: {b} \n"
    return HttpResponse(output)
