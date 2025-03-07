<?php
include('db.php'); // Include database connection

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);

    // Query the database for the username
    $sql = "SELECT * FROM users WHERE username = '$username'";
    $result = mysqli_query($conn, $sql);

    // Check if user exists
    if (mysqli_num_rows($result) > 0) {
        $row = mysqli_fetch_assoc($result);

        // Verify password
        if (password_verify($password, $row['password'])) {
            session_start();
            $_SESSION['username'] = $username;
            echo "Login successful! Welcome, " . $_SESSION['username'] . ".";
            // Redirect to dashboard (or air quality page)
        } else {
            echo "Invalid password.";
        }
    } else {
        echo "User not found.";
    }

    // Close the database connection
    mysqli_close($conn);
}
?>
