function sendMessage() {
    const userText = $("#userInput").val().trim();

    if (userText === "") return;

    $("#chatbox").append(`<div class='user'><strong>You:</strong> ${userText}</div>`);
    $("#userInput").val("");

    $.ajax({
        url: "/ask",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ msg: userText }),
        success: function(response) {
            $("#chatbox").append(`<div class='bot'><strong>Bot:</strong> ${response.reply}</div>`);
            $("#chatbox").scrollTop($("#chatbox")[0].scrollHeight);
        },
        error: function() {
            $("#chatbox").append("<div class='bot'><strong>Bot:</strong> Sorry, something went wrong.</div>");
        }
    });
}

// Send message with Enter key
$(document).ready(function() {
    $("#userInput").keypress(function(event) {
        if (event.which === 13) {
            sendMessage();
            event.preventDefault();
        }
    });
});
