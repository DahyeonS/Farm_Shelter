$(function(){
    $('.top_button_box').on('click',function(){
        $('html, body').animate({
            scrollTop: 0
        }, 500);
        return false;
    })
    
    /* 스크롤이 올리는지 내리는지 감지 */
    let lastScroll = 0; // 초기 스크롤 위치
    $(window).scroll(function(){
        let nowScroll = $(this).scrollTop(); // 현재 스크롤 위치
        // 스크롤 내려갈때
        if (nowScroll > lastScroll) {
            $('.logo_box').css({
                position:'absolute',
                background: 'transparent',
                boxShadow:'0 0 20px 0 transparent'
            })
        } 
        // 스크롤 맨위 감지
        else if (nowScroll == 0) {
            $('.logo_box').css({
                position:'absolute',
                background: 'transparent',
                boxShadow:'0 0 20px 0 transparent'
            })
        } 
        // 스크롤 위로 올라갈때
        else { 
            $('.logo_box').css({
                position:'fixed',
                background: '#2C6E49',
                boxShadow:'0 0 20px 0 #333'
            })
        }

        if (nowScroll == 0) $('.top_button_box').css({display:'none'})
        else if (nowScroll >= 0) $('.top_button_box').css({display:'flex'})
        lastScroll = nowScroll; // 현재 스크롤 위치 할당
    });

    /* 햄버거 버튼 클릭시 js */
    let clickCount = 0;
    $('.ham_button').on('click',function(){
        clickCount++;
        if (clickCount % 2 === 1) {
            $('.mobile_ham_box').css({
                right: '0px',
            })
        } else {
            $('.mobile_ham_box').css({
                right: '-290px'
            })
		}
    })

    /* 데스크 화면에서 mypage 버튼 */
    let clickCount2 = 0;
    $('.mypage').on('click', function(){
        clickCount2++;
        if (clickCount2 % 2 === 1) {
            $('.li_side_menu_box').css({
                height: '222px'
            })
        } else {
            $('.li_side_menu_box').css({
                height: '0px'
            })
        }
    })

    // 우측 마우스 클릭, 드래그 금지
    $(document).bind("contextmenu", function(e){return false;});
    $(document).bind('selectstart', function(){return false;}); 
    $(document).bind('dragstart', function(){return false;});

})