from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def detail(request, book_id):
    return HttpResponse(f"You're looking at book: {Book.objects.get(pk=book_id)}")
