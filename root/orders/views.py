from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import Order
from django.core.mail import send_mail


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


def cart(request):
    return render(request, 'orders/order_book.html', context={
        'title': 'Управління кошиком',
        'page': 'order_book',
        'app': 'orders',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })


def del_order(request, order_id):
    delete_order = Order.objects.get(id=order_id)
    delete_order.delete()
    return redirect('cart')


def confirm(request):
    if request.method == 'GET':
        return render(request, 'orders/confirm.html', context={
            'title': 'Підтвердження замовлення',
            'page': 'cofirm',
            'app': 'orders',
        })
    else:
        email = request.POST.get('email')
        info_list = []
        orders = Order.objects.filter(user_id=request.user.id)
        # -> 
        for order in orders:
            info_list.append({
                'order_title': order.title,
                'product_name': order.products,
                'product_price': order.price,
                'product_amount': order.amount
            })
        # -> 
        subject = 'Повідомлення про замовлення'
        body = f'''
            <h1>{subject}</h1>
            <hr />
            <h2 style="color: black">Ви підтвердили замовлення наступних товарів</h2>
            <h3>
            <ol>
        '''
        # -> 
        for item in info_list:
            body += f'''
                <li>
                №{item.get('order_title')} 
                {item.get('product_name')} 
                {item.get('product_amount')}шт 
                {item.get('product_price')}грн
                </li>  
            '''
        # -> 
        body += f'''
        </ol>
        </h3>
        <hr />
        '''
        # -> 
        success = send_mail(subject, '', 'DeliniTime.@gmail.com', [email], fail_silently=False, html_message=body)
        if success: 
            return render(request, 'orders/thanks.html', context={
                'title': 'Подяка за замовлення',
                'page': 'thanks',
                'app': 'orders',
                'email': email
            })
        else:
            return render(request, 'orders/failed.html', context={
                'title': 'Помилка поштового відправлення',
                'page': 'failed',
                'app': 'orders',
            })








# def bill(request, sel_list: str):
#     # -> 
#     sel_list_str = sel_list.split(',')
#     sel_list_num = [int(x) for x in sel_list_str[:-1]]
#     total_price = int(sel_list_str[-1])
#     final_list = []
#     # -> 
#     for order_id in sel_list_num:
#         order = Order.objects.get(id=order_id)
#         final_list.append({
#             'product_name': order.products.name,
#             'product_price': order.products.price,
#         })
#     # -> 
#     return render(request, 'orders/bill.html', context={
#         'title': 'Сторінка замовлення',
#         'page': 'bill',
#         'app': 'orders',
#         'total_price': total_price,
#         'final_list': final_list,
#         'init_list': sel_list,
#     })