from django.urls import path
from . import views

app_name = 'book_list'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<int:book_id>/detail/', views.detail, name='detail'),
    path('list/', views.view, name='list'),
    path('delete/', views.delete, name='delete'),
    path('delete_list/', views.delete_list, name='delete_list'),
    path('add', views.add, name='add'),
    path('add_book', views.add_book, name='add_book'),
    path('edit_list', views.edit_list, name='edit_list'),
    path('<int:book_id>/edit/', views.edit, name='edit'),
    path('<int:book_id>/edit_book/', views.edit_book, name='edit_book'),
]
