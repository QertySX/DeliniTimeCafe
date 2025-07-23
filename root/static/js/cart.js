$(document).ready(() => {
    // Check
  console.log('cart.js -> Start');

    
    // 1 
    $('.filters-content').on('click', '.add-to-cart-btn', (event) => {
        console.log('add-btn -> Click');
        const button = $(event.target).closest('.add-to-cart-btn');

        // 2 
        let userId = $('#user-id').val();
        console.log('userId: ', userId)
        // 3
        if (userId == 'None') {
            alert('Для використання кошику Ви повинні авторизуватись')
        } else {
            // 4
            let productId = button.siblings('input[type="hidden"]').val();
            console.log('productId:', productId);

            // 5 
            let productPrice = parseFloat(button.closest('.options').find('h6').text());
            console.log('productPrice:', productPrice);

            // Ajax-запит до серера на збереження товару до БД (таблиця кошика)
            $.ajax({
                url: '/orders/ajax_cart',
                data: `uid=${userId}&pid=${productId}&price=${productPrice}`,
                success: (result) => {
                    console.log('Ajax -> Ok');
                    console.log(result.message);
                    console.log('Check data:');
                    // -> 
                    console.log('uid: ', result.uid);
                    console.log('pid: ', result.pid);
                    console.log('price: ', result.price);
                }
            })
        }
  });
});
