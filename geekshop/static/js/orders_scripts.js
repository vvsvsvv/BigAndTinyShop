let _quantity, _price, orderitemNum, deltaQuantity, orderitemQuantity, deltaCost;
let quantityArr = [];
let priceArr = [];
let orderForm;
let orderTotalQuantity;
let orderTotalCost;

function orderSummaryUpdate(orderitemPrice, deltaQuantity) {
    deltaCost = orderitemPrice * deltaQuantity;
 
    orderTotalCost = Number((orderTotalCost + deltaCost).toFixed(2));
    orderTotalQuantity = orderTotalQuantity + deltaQuantity;
 
    $('.order_total_cost').html(orderTotalCost.toString());
    $('.order_total_quantity').html(orderTotalQuantity.toString());
 }

window.onload = function () {
    orderForm = $('.order_form')
    let TOTAL_FORMS = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());

    orderTotalQuantity = parseInt($('.order_total_quantity').text()) || 0;
    orderTotalCost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;

    for (let i=0; i < TOTAL_FORMS; i++) {
    _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
    _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
    quantityArr[i] = _quantity;
    priceArr[i] = _price || 0
    }
    // console.log(quantityArr)
    // console.log(priceArr)
    if (!orderTotalQuantity) {
        for (let i=0; i < TOTAL_FORMS; i++) {
            orderTotalQuantity += quantityArr[i];
            orderTotalCost += quantityArr[i] * priceArr[i];
        }
        $('.order_total_quantity').html(orderTotalQuantity.toString());
        $('.order_total_cost').html(Number(orderTotalCost.toFixed(2)).toString());
    }

    orderForm.on('change', 'input[type="number"]', function (event) {
        var target = event.target;
        orderitemNum = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (priceArr[orderitemNum]) {
            orderitemQuantity = parseInt(target.value);
            deltaQuantity = orderitemQuantity - quantityArr[orderitemNum];
            quantityArr[orderitemNum] = orderitemQuantity;
            orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
        }
     });
     
    orderForm.on('click', 'input[type="checkbox"]', function (event) {
        var target = event.target;
        orderitemNum = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));
        if (target.checked) {
            deltaQuantity = -quantityArr[orderitemNum];
        } else {
            deltaQuantity = quantityArr[orderitemNum];
        }
        orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
     });
}