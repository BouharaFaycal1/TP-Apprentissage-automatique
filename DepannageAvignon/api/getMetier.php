<?php

/*
* APi qui renvoie le json des utilsateurs ainsi que les artisans gagnants de chaque ville 
*
*/
    header('charset=utf-8');
    include("config.php");
   
    $query = 'select * from metier';
    $result = $con->query($query);
    $res['metier']= [];
    while($cat = $result->fetch_assoc()){
        $res['metier'][]= $cat;
    }
 
    echo json_encode($res);