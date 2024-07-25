<?php
if ($_POST['username'] == "admin" && $_POST['password'] == "password" ){
    header("Location: goodjobfindingme.html");
    exit();
}
else{
    header("Location: login.html");
    exit();
}
?>