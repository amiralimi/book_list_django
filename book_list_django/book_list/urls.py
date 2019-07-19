from django.urls import path
from . import views

app_name = 'book_list'
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<int:book_id>/detail/', views.detail, name='detail'),
    path('list/', views.view, name='list'),
    path('delete/', views.delete, name='delete'),
    path('delete_list/', views.delete_list, name='delete_list'),
]
