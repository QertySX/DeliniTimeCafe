from django.urls import path
from .views import index, about, book, done, del_reserv, add_reviews, del_review, edit_review

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('book_table', book, name='book_table'),
    path('done', done, name='done'),
    path('delete-reserve/<int:book_table_id>/', del_reserv, name='del_reserv'),
    path('add_reviews', add_reviews, name='add_reviews'),
    path('del_review/<int:reviews_id>/', del_review, name='del_review'),
    path('edit_review/<int:reviews_id>/', edit_review, name='edit_review')
]