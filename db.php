<?php
$servername = "localhost";  // Default server name for XAMPP
$username = "root";        // Default username for MySQL in XAMPP
$password = "";            // Default password for MySQL in XAMPP
$dbname = "air_quality";   // Database name we created earlier

// Create the connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check if the connection was successful
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
