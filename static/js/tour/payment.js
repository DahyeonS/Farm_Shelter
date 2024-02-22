const csrfToken = $('meta[name="csrf_token"]').attr('content');

function pay() {
    const name = $('#name').val()
    const email = $('#email').val()
    const tourName = $('#tour_name').val()
    const tourId = $('#tour_id').val()
    const reservationId = $('#reservation_id').val()
    const price = $('#price').val().split('원')[0];

    IMP.init(impCode)
    IMP.request_pay({
        pg : 'kakaopay',
        pay_method : 'card',
        merchant_uid : `tour${tourId}_` + new Date().getTime(),
        name : tourName,
        amount : price,
        buyer_email : email,
        buyer_name : name,
        buyer_tel : '010-1234-5678',
        buyer_addr : '서울특별시 강남구 삼성동',
        buyer_postcode : '123-456',
    }, function(rsp) {
        if (rsp.success) {
            const uid = rsp.merchant_uid;
            const impUid = rsp.imp_uid;
            const amount = rsp.paid_amount;
            const params = {reservationId, uid, impUid, amount}

            $.ajax({
                type:'POST',
                url: '../payment/' + reservationId,
                dataType: 'json',
                data: params,
                headers: {"X-CSRFToken": csrfToken},
                success: function(data){
                    if (data['rs'] === 1) location.href = '../payment_result/' + reservationId;
                },
                error: function(xhr, status, error) {
                    console.log(xhr, status, error);
                }
            });
        } else alert(`결제에 실패하였습니다. ${rsp.error_msg}`);
    });
}

