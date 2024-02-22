function trustHtml(str) {
    return $('<div />').html(str).text();
}

$(function() {
    $('#story').html(trustHtml(story))
    $('#recipe').html(trustHtml(recipe))

    $('.bs_1').css({
        background: `url(${url_1})`,
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
    })

    $('.bs_2').css({
        background: `url(${url_2})`,
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat'
    })
})