<?php
$servername = "localhost";
$username = "pi";
$password = "12345";
$dbname = "sensor";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT lightning,state from data";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<br><h1 class='card-title pricing-card-title'>". $row["lightning"]."<br><small class='text-muted'>µg/m3 </small>"."</h1> <br>
        <br><h1 class='card-title pricing-card-title'>". $row["state"]."<br><small class='text-muted'>µg/m3 </small>"."</h1> <br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
