<?php
include('../libs/connection.php');    
if (isset($_POST['message']) && !empty($_POST['message'])) {
    $message = $_POST['message'];
    $sender = "User"; // Thay đổi thành tên người dùng hoặc ID của bạn
    
    $sql = "INSERT INTO messages (sender, message) VALUES ('$sender', '$message')";
    $db->query($sql);
    $db->close();
}
?>
