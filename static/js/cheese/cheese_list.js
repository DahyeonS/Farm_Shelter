$(function() {
	$('#not').css({background:'#4c956c', color:'#fff'})
	cheese_paging(1)
	
	$('.kb_name').on('click', function(){
		const id = $(this).attr('id');
		$(this).css({background:'#4c956c', color:'#fff'})
		$('.kb_name').not(this).css({background:'#ddd', color: '#333'})

		if (id !== 'not') cheese_subject(id)
		else cheese_paging(1)
	})
})

function paging(page, pageRange) {
    let text = `<ul>`

    for (pageNum of pageRange) {
        if (pageNum !== page) text += `<li><a href="javascript:void(0)" onclick="cheese_paging(${pageNum})">${pageNum}</a></li>`;
        else text += `<li><span>${pageNum}</span></li>`;
    }
    
    text += `</ul>`;
    return text
}

function cheese_paging(page) {
	$('.paging').show();
	const param = {page}

    $.ajax({
		type: 'GET',
		url: '../ajax/cheesePaging',
		dataType: 'json',
		data: param,
		success: function(data) {
			let list = ''

            for (let i=0; i<data['items'].length; i++) {
				const {id, name, url} = data['items'][i]
				list += `<div class="content_box"><a class="content_photo" href="detail/${id}"><img src="${url.split(', ')[0]}"></a>
				<span><a href="detail/${id}">${name} 치즈</a></span></div>`
			}

			const {pageRange} = data
			const text = paging(page, pageRange)
			
			$('.cb_con_box').html(list);
			$('#paging').html(text);
		},
		error: function(xhr, status, error) {
            console.log(xhr, status, error);
		}
	});
}

function cheese_subject(sub){
	$('.paging').hide();
	const param = {sub}

	$.ajax({
		type:'GET',
		url: '../ajax/cheeseSubject',
		dataType: 'json',
		data: param,
		success: function(data){
			let list = ``;

			for(d of data) {
				const {id, name, url} = d
				list += `<div class="content_box"><a class="content_photo" href="detail/${id}"><img src="${url.split(', ')[0]}"></a>
				<span><a href="detail/${id}">${name} 치즈</a></span></div>`
			}

			$('.cb_con_box').html(list);
		},
		error: function(xhr, status, error) {
            console.log(xhr, status, error);
		}
	});
}