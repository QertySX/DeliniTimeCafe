from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Order


def ajax_cart(request):
    response = dict()
    response['message'] = 'Hello from server!'

    uid = request.GET['uid']
    pid = request.GET['pid']
    price = request.GET['price']

    response['uid'] = uid
    response['pid'] = pid
    response['price'] = price

    # 1 - Створення нового замовлення та збереження у БД :

    Order.objects.create(
        title=f'Order-{pid}/{uid}/{timezone.now()}',
        amount=1,
        user_id=uid,
        products_id=pid,
        price=price
    )
    # 2 - Зчитуємо із бази список всіх замовлень даного користувача
    user_orders = Order.objects.filter(user_id=uid)

    # відправляємо дані клієнту:
    return JsonResponse(response)


def ajax_cart_indicate(request):
    response = dict()
    uid = request.GET['uid']
    user_orders = Order.objects.filter(user_id=uid)
    # -> 
    total_price = 0
    for order in user_orders:
        total_price += order.price
    # -> 
    response['total_price'] = total_price
    return JsonResponse(response)


def reserv(request):
    return render(request, 'orders/order_book.html', context={
        'title': 'Управління кошиком',
        'page': 'index',
        'app': 'orders',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })