<?php
    $server_name = "localhost";
    $user_name = "fafa";
    $password = "test";
    $db = "depannageavignon";

    $con = mysqli_connect($server_name, $user_name, $password, $db);

    if( !$con ){
        die("Connection Error");
    }
?>