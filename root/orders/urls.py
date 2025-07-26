from django.urls import path, re_path
from .views import ajax_cart, cart, ajax_cart_indicate, del_order, confirm

urlpatterns = [
    path('order_book', cart, name='cart'),
    path('ajax_cart', ajax_cart),
    path('ajax_cart_indicate', ajax_cart_indicate),
    # re_path(f'^bill/(?P<sel_list>[0-9\,]+)$', bill),
    path('delete-order/<int:order_id>/', del_order, name='del_order'),
    path('confirm', confirm, name='confirm')
]