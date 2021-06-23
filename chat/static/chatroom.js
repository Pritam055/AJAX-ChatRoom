
const username = document.getElementById("usernameId").getAttribute("data-username")
const room_name = document.getElementById("room_name_id").getAttribute('data-room')
$(document).ready(function () {
    let val = setInterval(function () {
        $.ajax({
            method: "GET",
            url: "/all-messages/" + room_name + "/",
            success: function (response) {
                let temp = "";
                let displayMessage = $("#displayMessage")
                displayMessage.empty()
                response.message_list.forEach(msg => {
                    if(username === msg.user ){
                        temp = "<div><b> >>" + msg.user + "</b> : " + msg.body + "</div>"
                    }else{
                        temp = "<div><b>" + msg.user + "</b> : " + msg.body + "</div>"
                    }
                    
                    displayMessage.append(temp)
                })
            },
            error: function (err) {
                console.log("ERror: ", err)
            }
        })
    }, 1000);
})

function goBack(){
    window.history.back();
}

$(document).on('submit', '#messageFormId', (e) => {
    e.preventDefault();
    const message = document.querySelector("input[name=message]").value
    const csrf = document.querySelector('input[name=csrfmiddlewaretoken]').value
    const mydata = {
        body: message,
        username: username,
        room_name: room_name,
        csrfmiddlewaretoken: csrf
    }
    $.ajax({
        method: 'POST',
        url: '/send-message/',
        data: mydata,
        success: function (response) { 
            document.querySelector('#messageFormId').reset()
        },
        error: function (err) {
            console.log("ErroR: ", err)
        }
    })
})



