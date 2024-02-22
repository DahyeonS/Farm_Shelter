const url_1 = url_zip.split(', ')[0]
let url_2, url_3, url_4, url_5 = ''

if (url_zip.split(', ').length > 1) url_2 = url_zip.split(', ')[1]
if (url_zip.split(', ').length > 2) url_3 = url_zip.split(', ')[2]
if (url_zip.split(', ').length > 3) url_4 = url_zip.split(', ')[3]
if (url_zip.split(', ').length > 4) url_5 = url_zip.split(', ')[4]
    
function trustHtml(str) {
    return $('<div />').html(str).text();
}

$(function() {
    $('#story').html(trustHtml(story))
    $('#special').html(trustHtml(special))
    $('#link').html(trustHtml(link))

    $('.sp_1').css({
        background: `url(${url_1})`,
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
    })

    $('.sp_2').css({
        background: `url(${url_2})`,
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
    })

    $('.sp_3').css({
        background: `url(${url_3})`,
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
    })

    $('.sp_3').css({
        background: `url(${url_3})`,
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
    })

    $('.sp_4').css({
        background: `url(${url_4})`,
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
    })

    $('.sp_5').css({
        background: `url(${url_5})`,
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
    })

    /* 메인 슬라이드 - farm */
    const swiper2 = new Swiper(".mySwiper.farm", {
        spaceBetween: 30,
        loop: true,
        autoplay: true,
        effect: "fade",
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });

    // 목장 로고가 있을때 없을때
    $('.farm_logo_link_box a').each(function() {
        const hasImg = $(this).find('img').length > 0;

        if (hasImg) {
            $(this).find('span').removeClass('link_span_img_nothing');
        } else {
            $(this).find('span').addClass('link_span_img_nothing');
        }
    });

    // 목장 요거트 옆에 설명이 있을때와 없을때
    $('.fs_story_box').each(function() {
        const hasText = $(this).find('.story_text_box').length > 0;

        if (hasText) {
            $('.farm_story_map_box_flex').css({
                display: 'flex',
                flexDirection: 'column',
                width: '100%',
                gap: '60px'
            })
            $('.farm_special_box').css({width: '100%'})
            $('.farm_map_box').css({width: '100%'})
            $('.fs_photo_box').css({width:'35%'})
        } else {
            $('.farm_story_map_box_flex').css({
                display: 'flex',
                flexDirection: 'row',
                width: '100%',
                gap: '20px'
            })
            $('.farm_special_box').css({width: '50%'})
            $('.farm_map_box').css({width: '50%'})
            $('.fs_photo_box').css({width:'80%'})
        }
    });
})