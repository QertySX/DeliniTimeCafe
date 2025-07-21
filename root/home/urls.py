from django.urls import path
from .views import index, about, book

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('book_table', book, name='book_table')
]