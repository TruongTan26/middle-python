<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <?php include('./libs/header.php')?>
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
                $.post("./libs/send_message.php", { message: message }, function() {
                    loadMessages();
                    $("#message").val("");
                });
            });
            
            function loadMessages() {
                $.get("./libs/get_messages.php", function(data) {
                    $("#chat-box").html(data);
                });
            }
        });
    </script>
</body>
</html>