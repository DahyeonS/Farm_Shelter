const csrfToken = $('meta[name="csrf_token"]').attr('content');

function loginCheck() {
    return username !== '';
}

function replyBtnFunctionQuestion(id, username) {
    const param = {id}

    $.ajax({
        type:'GET',
        url: '../../ajax/questionReply',
        dataType: 'json',
        data: param,
        success: function(data){
            let reply = ``;

            data.reply.forEach(function(replyItem) {
                if(id == replyItem.question_id) {
                    const de = replyItem;
                    const createdDate = new Date(de.created_date);
                    const formate_create_date = createdDate.toLocaleString('ko-KR', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                        hour: 'numeric',
                        minute: 'numeric',
                        hour12: true
                    });

                    const modifiedDate = new Date(de.modified_date);
                    const formate_modified_date = modifiedDate.toLocaleString('ko-KR', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                        hour: 'numeric',
                        minute: 'numeric',
                        hour12: true
                    });
                    reply += `<div class="reply_box"><div class="question_flex line_span"><span class="user_flex">${de.username}</span>
                    <div class="date_btn_box"><span style="font-size: 12px;">`;

                    if (de.modified_date == null) reply += formate_create_date
                    else reply += formate_modified_date

                    reply +=`</span></div></div><span class="q_content" style="padding: 5px 30px; box-sizing: border-box;">${de.content}</span>`
                    if (replyItem.username == username || replyItem.username == 'admin') {
                        `<span class="update_delete_btn"><input type="button" value="수정" id="qrupdate${de.id}" onclick="showQReplyUpdate(${de.id});">
                        <div class="multibox"><form id="qReplyUpdate${de.id}"><textarea name="content" cols="30" rows="10">${de.content}</textarea>
                        <input type="button" value="수정" onclick="updateQReply(${de.id});"></form>
                        <input type="button" value="삭제" onclick="deleteQReply(${de.id});" class="danger_btn"></div></span>`;
                    }
                    reply += `</div>`;
                } 
            });

            $('#question_reply'+id).html(reply);
            $('#close'+id).html('close');
        },
        error: function(xhr, status, error) {
            console.log(xhr, status, error);
        }
    });
}

function moreBtnFunctionQuestion(id) {
    const param = {id}

    $.ajax({
        type:'GET',
        url: '../../ajax/questionReply',
        dataType: 'json',
        data: param,
        success: function(data){
            let remoreIds = []
            $('.question_div').each(function() {
                const id = $(this).attr('id').split('question')[1]; 
                remoreIds.push(id);
            });
            
            for (let remoreId of remoreIds) {
                for (let i = 0; i < data.reply.length; i++) {
                    const idname = data.reply[i].question_id;
                    if (remoreId.includes(idname)) $(`#more${idname}.question_more`).html('more');
                }
            }
        },
        error: function(xhr, status, error) {
            console.log(xhr, status, error);
        }
    });
}

function replyBtnFunction(id, username) {
    console.log(username);
    const param = {id}

    $.ajax({
        type:'GET',
        url: '../../ajax/reviewReply',
        dataType: 'json',
        data: param,
        success: function(data){
            let reply = ``;

            data.reply.forEach(function(replyItem) {
                if (id == replyItem.review_id) {
                    const de = replyItem;
                    const createdDate = new Date(de.created_date);
                    const formate_create_date = createdDate.toLocaleString('ko-KR', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                        hour: 'numeric',
                        minute: 'numeric',
                        hour12: true
                    });

                    const modifiedDate = new Date(de.modified_date);
                    const formate_modified_date = modifiedDate.toLocaleString('ko-KR', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric',
                        hour: 'numeric',
                        minute: 'numeric',
                        hour12: true
                    });

                    reply += `<div class="reply_box"><div class="review_flex line_span"><span class="user_flex">${de.username}</span>
                    <div class="date_btn_box"><span style="font-size: 12px;">`;

                    if (de.modified_date == null) reply += formate_create_date
                    else reply += formate_modified_date

                    reply += `</span></div></div><span class="r_content" style="padding: 5px 30px; box-sizing: border-box;">${de.content}</span>`
                    if (replyItem.username == username || replyItem.username == 'admin') {
                        reply += `<span class="update_delete_btn"><input type="button" value="수정" id="rrupdate${de.id}" onclick="showRReplyUpdate(${de.id});">
                        <div class="multibox"><form id="rReplyUpdate${de.id}"><textarea name="content" cols="30" rows="10">${de.content}</textarea>
                        <input type="button" value="수정" onclick="updateRReply(${de.id});"></form>
                        <input type="button" value="삭제" onclick="deleteRReply(${de.id});" class="danger_btn"></div></span>`;
                    }
                    reply += `</div>`;
                } 
            });
            $('#review_reply'+id).html(reply);
            $('#close'+id).html('close');
        },
        error: function(xhr, status, error) {
            console.log(xhr, status, error);
        }
    });
}

function moreBtnFunction(id) {
    const param = {id}

    $.ajax({
        type:'GET',
        url: '../../ajax/reviewReply',
        dataType: 'json',
        data: param,
        success: function(data){
            let remoreIds = [];

            $('.review_div').each(function() {
                const id = $(this).attr('id').split('review')[1]; 
                remoreIds.push(id);
            });
            
            for (let remoreId of remoreIds) {
                for (let i = 0; i < data.reply.length; i++) {
                    let idname = data.reply[i].review_id;
                    if (remoreId.includes(idname)) $('#more'+idname).html('more');
                }
            }
        },
        error: function(xhr, status, error) {
            console.log(xhr, status, error);
        }
    });
}

function showRReply(id) {
    if (loginCheck()) {
        $('#rReply' + id).show();
        $('#rrwrite' + id).hide();
    } else alert('로그인이 필요합니다.');
}

function showQReply(id) {
    if (loginCheck()) {
        $('#qReply' + id).show();
        $('#qrwrite' + id).hide();
    } else alert('로그인이 필요합니다.');
}

function showReviewUpdate(id, rate) {
    if (loginCheck()) {
        $('#review_update' + id).css('display','flex');
        $('#review' + id).hide();
        $('#rupdate' + id).hide();
        $(`#review_update${id} .rate input[value="${parseFloat(rate)}"]`).attr('checked', true);
    } else alert('로그인이 필요합니다.');
}

function showQuestionUpdate(id) {
    if (loginCheck()) {
        $('#question_update' + id).css('display','flex');
        $('#question' + id).hide();
        $('#qupdate' + id).hide();
        $(`#question_update${id} .rate input[value="${parseFloat(rate)}"]`).attr('checked', true);
    } else alert('로그인이 필요합니다.');
}

function showRReplyUpdate(id) {
    if (loginCheck()) {
        $('#rReplyUpdate' + id).show();
        $('#review_reply' + id).hide();
        $('#rrupdate' + id).hide();
    } else alert('로그인이 필요합니다.');
}

function showQReplyUpdate(id) {
    if (loginCheck()) {
        $(`#qReplyUpdate` + id).show();
        $(`#qReply` + id).show();
        $('#question_reply' + id).hide();
        $('#qrupdate' + id).hide();
    } else alert('로그인이 필요합니다.');
}

function writeReview(id) {
    const form = $('#review')[0]
    const formData = new FormData(form)

    const content = $('#review textarea').val()
    const photo = $('#review input[name=photo]')[0].files
    const rate = $('#review .rate input[name="rating"]:checked').val();

    if (content.length === 0) alert('내용을 입력해주세요.')
    else if (rate === undefined) alert('평점을 입력해주세요.')
    else {
        formData.append("tour_id", id)
        formData.append("content", content)
        formData.append("photo", photo)
        formData.append("rate", rate)

        $.ajax({
            type:'POST',
            url: '../../ajax/writeReview',
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            data: formData,
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function updateReview(id) {
    const form = $('#review_update' + id)[0]
    const formData = new FormData(form)

    const content = $(`#review_update${id} textarea`).val()
    const photo = $(`#review_update${id} input[name=photo]`)[0].files
    const rate = $(`#review_update${id} .rate input[name="rating"]:checked`).val();
    const fileDelete = $(`#review_update${id} input[name=fileDelete]:checked`).val();

    if (content.length === 0) alert('내용을 입력해주세요.')
    else {
        formData.append("id", id)
        formData.append("content", content)
        formData.append("photo", photo)
        formData.append("rate", rate)
        formData.append("fileDelete", fileDelete)
    }

    $.ajax({
        type:'POST',
        url: '../../ajax/updateReview',
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        data: formData,
        success: function(data){
            if (data['rs'] === 1) location.reload();
        },
        error: function(xhr, status, error) {
            console.log(xhr, status, error);
        }
    });
}

function deleteReview(id) {
    const param = {id}

    if (confirm('정말 삭제하시겠습니까?')) {
        $.ajax({
            type:'POST',
            url: '../../ajax/deleteReview',
            dataType: 'json',
            data: param,
            headers: {"X-CSRFToken": csrfToken},
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function writeRReply(id) {
    const form = $('#rReply' + id)[0]
    const formData = new FormData(form)
    const content = $(`#rReply${id} textarea`).val();

    if (content.length === 0) alert('내용을 입력해주세요.')
    else {
        formData.append("review_id", id)
        formData.append("content", content)

        $.ajax({
            type:'POST',
            url: '../../ajax/writeReviewReply',
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            data: formData,
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function updateRReply(id) {
    const form = $('#rReplyUpdate' + id)[0]
    const formData = new FormData(form)
    const content = $(`#rReplyUpdate${id} textarea`).val();

    if (content.length === 0) alert('내용을 입력해주세요.')
    else {
        formData.append("id", id)
        formData.append("content", content)

        $.ajax({
            type:'POST',
            url: '../../ajax/updateReviewReply',
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            data: formData,
            headers: {"X-CSRFToken": csrfToken},
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function deleteRReply(id) {
    const param = {id}

    if (confirm('정말 삭제하시겠습니까?')) {
        $.ajax({
            type:'POST',
            url: '../../ajax/deleteReviewReply',
            dataType: 'json',
            data: param,
            headers: {"X-CSRFToken": csrfToken},
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function writeQuestion(id) {
    const form = $('#question')[0]
    const formData = new FormData(form)

    const content = $('#question textarea').val()
    const photo = $('#question input[name=photo]')[0].files
    
    if (content.length === 0) alert('내용을 입력해주세요.')
    else {
        formData.append("tour_id", id)
        formData.append("content", content)
        formData.append("photo", photo)

        $.ajax({
            type:'POST',
            url: '../../ajax/writeQuestion',
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            headers: {"X-CSRFToken": csrfToken},
            data: formData,
            success: function(data){
                if(data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function updateQuestion(id) {
    const form = $('#question_update' + id)[0]
    const formData = new FormData(form)

    const content = $(`#question_update${id} textarea`).val()
    const photo = $(`#question_update${id} input[name=photo]`)[0].files
    const fileDelete = $(`#question_update${id} input[name=fileDelete]:checked`).val();

    if (content.length === 0) alert('내용을 입력해주세요.')
    else {
        formData.append("id", id)
        formData.append("content", content)
        formData.append("photo", photo)
        formData.append("fileDelete", fileDelete)
    }

    $.ajax({
        type:'POST',
        url: '../../ajax/updateQuestion',
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        data: formData,
        success: function(data){
            if (data['rs'] === 1) location.reload();
        },
        error: function(xhr, status, error) {
            console.log(xhr, status, error);
        }
    });
}

function deleteQuestion(id) {
    const param = {id}

    if (confirm('정말 삭제하시겠습니까?')) {
        $.ajax({
            type:'POST',
            url: '../../ajax/deleteQuestion',
            dataType: 'json',
            data: param,
            headers: {"X-CSRFToken": csrfToken},
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function writeQReply(id) {
    const form = $('#qReply' + id)[0]
    const formData = new FormData(form)
    const content = $(`#qReply${id} textarea`).val();

    if (content.length === 0) alert('내용을 입력해주세요.')
    else {
        formData.append("question_id", id)
        formData.append("content", content)

        $.ajax({
            type:'POST',
            url: '../../ajax/writeQuestionReply',
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            data: formData,
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function updateQReply(id) {
    const form = $('#qReplyUpdate' + id)[0]
    const formData = new FormData(form)
    const content = $(`#qReplyUpdate${id} textarea`).val();

    if (content.length === 0) alert('내용을 입력해주세요.')
    else {
        formData.append("id", id)
        formData.append("content", content)

        $.ajax({
            type:'POST',
            url: '../../ajax/updateQuestionReply',
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            data: formData,
            headers: {"X-CSRFToken": csrfToken},
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

function deleteQReply(id) {
    const param = {id}

    if (confirm('정말 삭제하시겠습니까?')) {
        $.ajax({
            type:'POST',
            url: '../../ajax/deleteQuestionReply',
            dataType: 'json',
            data: param,
            headers: {"X-CSRFToken": csrfToken},
            success: function(data){
                if (data['rs'] === 1) location.reload();
            },
            error: function(xhr, status, error) {
                console.log(xhr, status, error);
            }
        });
    }
}

$(function() {
    let review_div_id = []
    let question_div_id = []
    let clickCount = 0;
    let clickCount2 = 0;

    $('.tour_content_box').html($('<div />').html(code).text());

    $('#rbutton').click(function() {
        if (loginCheck()) {
            $('#review').show();
            $('#rbutton').hide();
        } else alert('로그인이 필요합니다.')
    });
    
    $('#qbutton').click(function() {
        if (loginCheck()) {
            $('#question').show();
            $('#qbutton').hide();
        } else alert('로그인이 필요합니다.')
    });

    $('.review_div').each(function(){
        const de = $(this).attr('id').split('review')[1];
        review_div_id.push(de);
    })

    $('.reply_more_btn_box.review_more').click(function(){
        clickCount++;
        const nameid = $(this).attr('id');
        if (clickCount % 2 === 1) {
            replyBtnFunction(nameid.split('more')[1], username);
            $(this).html('close');
        } else {
            $(this).html('more');
            $('.review_reply_div .reply_box').addClass('none_btn');
        }
    })
    
    $('.reply_more_btn_box.question_more').click(function(){
        clickCount2++;
        const nameid = $(this).attr('id');
        if (clickCount2 % 2 === 1) {
            replyBtnFunctionQuestion(nameid.split('more')[1], username);
            $(this).html('close');
        } else {
            $(this).html('more');
            $('.question_reply_div .reply_box').addClass('none_btn');
        }
    })

    /* 메인 슬라이드 - tour */
    const swiper = new Swiper(".mySwiper.tour", {
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

    moreBtnFunction(review_div_id);
    moreBtnFunctionQuestion(question_div_id);
})