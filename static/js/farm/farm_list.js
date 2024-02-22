$(function() {
    farm_paging(1)
})

function paging(page, pageRange) {
    let text = `<ul>`

    for (pageNum of pageRange) {
        if (pageNum !== page) text += `<li><a href="javascript:void(0)" onclick="farm_paging(${pageNum})">${pageNum}</a></li>`;
        else text += `<li><span>${pageNum}</span></li>`;
    }
    
    text += `</ul>`;
    return text
}

function farm_paging(page) {
	const param = {page}

    $.ajax({
		type: 'GET',
		url: '../ajax/farmPaging',
		dataType: 'json',
		data: param,
		success: function(data) {
			let list = ''

            for (let i=0; i<data['items'].length; i++) {
				const {id, name, url} = data['items'][i]

				list += `<div class="content_box"><a class="content_photo" href="detail/${id}">`

				if (id===1 || id===19) list += `<img src="${url.split(', ')[1]}">`
				else if (id===18) list += `<img src="${url.split(', ')[2]}">`
				else list += `<img src="${url.split(', ')[0]}">`

				list += `</a><span><a href="detail/${id}">${name}</a></span></div>`
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