from django.urls import path
from . import views

app_name = 'book_list'
urlpatterns = [
    path('<int:book_id>/detail/', views.detail, name='detail'),
    path('list/', views.view, name='list'),
]
