<!DOCTYPE html>
<html>
<head>
    <title>Realtime Chat</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div id="chat">
        <div id="chat-box"></div>
        <input type="text" id="message" placeholder="Nhập tin nhắn..." />
        <button id="send">Gửi</button>
    </div>
    <script>
        $(document).ready(function() {
            loadMessages();
            
            $("#send").click(function() {
                var message = $("#message").val();
                $.post("send_message.php", { message: message }, function() {
                    loadMessages();
                    $("#message").val("");
                });
            });
            
            function loadMessages() {
                $.get("get_messages.php", function(data) {
                    $("#chat-box").html(data);
                });
            }
        });
    </script>
</body>
</html>
