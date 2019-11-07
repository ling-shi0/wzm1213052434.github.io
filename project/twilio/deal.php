<?php
   header("Content-type: text/html; charset=utf-8");
    $account_sid = $_GET['account_sid'];
    $auth_token = $_GET['auth_token'];
    $place=$_GET['place'];
    $fromphone=$_GET['fromphone'];
    $tophone=$_GET['tophone'];
    $testJSON = array('account_sid' => $account_sid, 'auth_token' => $auth_token,'place' => $place,'tophone'=>$tophone,'fromphone'=>$fromphone);
    foreach ($testJSON as $key => $value) {
        $testJSON[$key] = urlencode($value);
    }
    file_put_contents('result.json', urldecode(json_encode($testJSON)));
    $log=shell_exec('python send/read.py');
    echo $log;
    echo 1;
?>