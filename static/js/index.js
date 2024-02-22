$(function() {
    // 새로고침하면 스크롤 맨위로 이동 코드
    window.onload = function(){
        setTimeout(function(){
            scrollTo(0,0);
        }, 100)
    }

    // 비디오의 scroll down 클릭 시 스크롤 이동 코드
    $('.circle').click(function(){
        const offset = $('.head').offset();
        const outheight = $('.head').outerHeight();
        $('html').animate({scrollTop : offset.top + outheight}, 1000);
    });
    
    /* 메인 슬라이드 - cheese recipe*/
    const swiper = new Swiper(".mySwiper.recipe", {
        slidesPerView: 3,
        spaceBetween: 30,
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        mousewheel: true,
        keyboard: true,
        breakpoints: {
            1500:{
                slidesPerView: 3,
                spaceBetween: 50,
            }, 1000:{
                slidesPerView: 2,
                spaceBetween: 50,
            }, 300: {
                slidesPerView: 1,
                spaceBetween: 60
            }, 100: {
                slidesPerView: 1,
                spaceBetween: 60
            }
        },
    });

    /* 메인 슬라이드 - pasture */
    var swiper2 = new Swiper(".mySwiper.pasture", {
        spaceBetween: 30,
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

    $('.cm_download_box').click(function() {
        $('#upload').click();
    })

    $('#upload').change(function() {
        $('#cheese').submit();
    })
})