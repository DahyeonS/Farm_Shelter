$(function(){
    const params = {cheeseKey}

    $.ajax({
		type:'GET',
		url: '../ajax/cheeseResult',
		dataType: 'json',
		data: params,
		success: function(data){
            $('.oneText').html(data['name'][0]);
            $('.cc_e_context_box').html($('<span>').html(data['info'][0]['content']));
            $('.cc_e_other_cheese_box').html(data['info'][0]['other_cheese']);
            $('.co_text_box_2').html(data['name'][1]);
            $('.co_text_box_3').html(data['name'][2]);
            $('.co_text_box_4').html(data['name'][3]);
		},
		error: function(xhr, status, error) {
            console.log(xhr, status, error);
		}
	});

    for (let i=1; i<3; i++) {
        $(`.pic${i}`).css({
            background: 'url(/static/img/cheese/result/' + cheeseKey[0] + `_${i}.jpg)`,
            backgroundPosition: 'center',
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat'
        });
    }

    for (let i=1; i<cheeseKey.length; i++) {
        const seq = ['two', 'three', 'four']
        $(`.co_${i}`).css({
            background: 'url(/static/img/cheese/result/' + cheeseKey[i] + '_1.jpg)',
            backgroundPosition: 'center',
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat'
        });
        $(`.cheese_${seq[i-1]}_box`).show();
        $(`#result_line_${i-1}`).show();
    }

    $('.onePersent').html(cheeseValue[0] + '%');
    for (let i=1; i<cheeseValue.length; i++) $(`.co_num_box_${i+1}`).html(cheeseValue[i] + '%');
})