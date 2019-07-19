from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>/detail', views.detail, name='detail'),
]