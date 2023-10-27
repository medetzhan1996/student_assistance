function subject_search(){
    var $select = $('#id_subject').selectize({
        valueField: 'title',
        labelField: 'title',
        searchField: 'title',
        placeholder: 'Поиск предмета ...',
        options: [],
        create: true,
        multiple: false,
        load: function(query, callback) {
            if (!query  || query.length < 2) return callback();
            $.ajax({
                url: '/directory/subject/search',
                type: 'GET',
                data: {
                    q: query
                },
                error: function() {
                    callback();
                },
                success: function(res) {
                    return callback(res);
                }
            })
        }
    })
}


var $modal = $('#universal-modal')
$(document).on('click','.open-universal-modal',function(){
    var $link = $(this);
    var url = $link.data('modal-url')
    var title = $link.data('modal-title')
    if (url && title) {
        event.preventDefault();
        $('.modal-title', $modal).text(title);
        $.ajax({
            url: url,
            type: 'GET',
            success: function(data) {
                $('#universal-modal-content').html(data)
                $modal.on('shown.bs.modal', function () {
                }).modal('show');
                $("#id_phone_number").mask("+7 (999) 999-99-99")
            }
        })
    }
});

$(document).on('submit','#form-universal-modal',function(){
    event.preventDefault()
    $.ajax({
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        data: new FormData(this),
        dataType: 'json',
        contentType: false,
        cache: false,
        processData:false,
        success: function(response) {
          if(!response.success){
            $('#form-universal-modal-content').html(response.form_html)
          }
          else{
            redirect_url = response.redirect_url
            if(redirect_url){
                location.href = redirect_url
            }
          }
        },
        error: function (response) {
            alert('erroeer....')
        }
    });
})

$(document).on('submit','#form-universal-multipart-modal',function(){
    event.preventDefault()
    $.ajax({
        data: $(this).serialize(),
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        success: function(response) {
          if(!response.success){
            $('#form-universal-modal-content').html(response.form_html)
          }
          else{
            redirect_url = response.redirect_url
            if(redirect_url){
                location.href = redirect_url
            }
          }
        },
        error: function (response) {
            alert('error....')
        }
    });
})


$(document).on('submit','#form-register-modal',function(){
    event.preventDefault()
    $.ajax({
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        data: new FormData(this),
        dataType: 'json',
        contentType: false,
        cache: false,
        processData:false,
        beforeSend: function(){
        },
        success: function(response) {
          if(!response.success){
            $('#form-demand-content').html(response.form_html)
            $('#form-register-content').html(response.register_form_html)
          }
          else{
            redirect_url = response.redirect_url
            if(redirect_url){
                location.href = redirect_url
            }
          }
        },
        error: function (response) {
        }
    });
})

$(document).on('click','#delete-one-message',function(){
    var message_count_text = $('#messages-count').text()
    var message_count_int = parseInt(message_count_text)
    message_count_int = message_count_int - 1
    var $link = $(this);
    var url = $link.data('url')
    var message_div = '#' + $link.data('message-div')
    $.ajax({
            url: url,
            type: 'POST',
            success: function(data) {
                $(message_div).addClass('d-none')
                $('#messages-count').html(message_count_int)
            }
        })
});

$(document).on('change','.type-selected',function(){
    $('.file-content').removeClass('d-none')
});
