<?php
    include("config.php");

$idMetier = $_GET['idMetier'];
   
    
   
    $query = 'select id from categories where id_metier = "'.$idMetier.'"';
    $result = $con->query($query);

    $res['categories']= [];

    while($cat = $result->fetch_assoc()){
        $res['categories'][]= $cat;
    }
 

    echo json_encode($res);