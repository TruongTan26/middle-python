<?php
include('../libs/connection.php');
$sql = "SELECT * FROM messages ORDER BY created_at ASC";
$result = $db->query($sql);

if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        echo "<strong>" . $row['sender'] . ":</strong> " . $row['message'] . "<br>";
    }
}

$db->close();
?>
