<?php
require_once('./SqlHelper.class.php');
class BaseObject{

}
$mySqlHelper=new SqlHelper();
$column_id=$_GET['column_id'];
$sql="select * from QGNews where column_id=".$column_id;
//echo $sql;
$mydata=$mySqlHelper->execute_dql2($sql);//数组
//echo count($mydata);
echo json_encode($mydata,JSON_UNESCAPED_UNICODE);
?>