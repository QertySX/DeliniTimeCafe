function doCalculate() {
    console.log('doCalculate() -> Call ')

    // 1 
    let checkedCells = $('.check:checked');
    let totalPrice = 0.0;
    let selIdList = '';

    // 2 
    for (let cell of checkedCells) {
        let parentRow = $(cell).parent().parent();
        totalPrice += parseFloat($(parentRow).find('td.price-cell').text())
        selIdList += $(parentRow).find('td.id-cell') + ',';
    }
    selIdList += totalPrice;

    // 3 
    console.log(`totalPrice: ${totalPrice}`);
    console.log(`selIdList: ${selIdList}`);
    $('#total').text(`${totalPrice.toFixed(2)}`);
    $('#bill-btn').attr(`href`, `/orders/bill/${selIdList}`)
}


$(document).ready(() => {
    // 1
    console.log('calc_orders.js -> Start');
    doCalculate();

    // 2
    $('.check').click(() => {
        console.log('input.chek - Click');
        doCalculate()
    })
})