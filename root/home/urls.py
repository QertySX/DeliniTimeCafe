from django.urls import path
from .views import index, about, book, done, del_reserv

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('book_table', book, name='book_table'),
    path('done', done, name='done'),
    path('delete-reserve/<int:book_table_id>/', del_reserv, name='del_reserv')
]