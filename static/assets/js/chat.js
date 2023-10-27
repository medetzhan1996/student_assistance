const roomId = JSON.parse(
    document.getElementById('room-split-1-id').textContent
)
const demandDistributionIdActive = JSON.parse(
    document.getElementById('room-split-2-id').textContent
)
const requestUser = JSON.parse(
    document.getElementById('request-user').textContent
)
const url = 'ws://' + window.location.host + '/ws/chat/' + roomId + '/room/'
const chatSocket = new WebSocket(url)

chatSocket.onmessage = function(event) {
    var output = ''
    const data = JSON.parse(event.data)
    var demandDistributionId = data.demand_distribution_id
    const dateOptions = {hour: 'numeric', minute: 'numeric', hour24: true};
    const datetime = new Date().toLocaleString('en', dateOptions);
    const isMe = data.user_from === requestUser;
    const source = isMe ? 'float-right other-message' : 'my-message';
    var is_active = demandDistributionIdActive == demandDistributionId
    if(is_active){
        output += '<li class="clearfix">' + '<div class="message ' + source + '">' +
        '<p style="margin-bottom: -5px">' + data.message + '</p>' +
        '<small style="display: block;font-size: 10px;color: silver;">' + datetime + '</small>' + '</div> ' + '</li>'
        $('#chat-content').append(output).animate({ scrollTop: 200000 }, "slow")
    }
    else{
        var notification_chat_id = '#notification-chat-' + demandDistributionId
        var notification_chat = parseInt($(notification_chat_id).html())
        if(notification_chat){
            notification_chat += 1
        }
        else{
            notification_chat = 1
        }
        $(notification_chat_id).html(notification_chat)

    }
}

chatSocket.onclose = function(event) {
    console.error('Chat socket closed unexpectedly')
}

$(document).on('keypress',function(e) {
    if(e.which == 13) {
        e.preventDefault()
        $('#chat-message-submit').click()
    }
})

$(document).on('click','#chat-message-submit',function(){
    const text = $('#chat-message-input').val()
    $.ajax({
        url: "/chat/message/create",
        type: 'POST',
        data: {
            text: text,
            object_id: demandDistributionIdActive
        },
        success: function(data) {
            $('#chat-message-input').val('').focus()
            chatSocket.send(JSON.stringify({
                'message': text, 'demand_distribution_id': demandDistributionIdActive,
                'type': 'chat_message', 'user_from': requestUser
            }))
        }
    })
})