<?php 
ini_set('memory_limit','-1');  #to increase memory limit
echo '<body style="background-color:#35B9A7">';
error_reporting(0);

$word= $_POST["query"];  #the query received from search bar is stored in this variable

$string1 = file_get_contents("invertedIndex.json");
$final1=json_decode($string1,true);

$string2=file_get_contents("urls_id.json");
$final2=json_decode($string2,true);

$pieces = explode(" ", $word);  #to split the query into seperate words

foreach ($pieces as &$value){
   if (array_key_exists($value,$final1)){
       foreach ($final1[$value] as $value1) {
       $url= $final2[$value1[0]];
       $url_end=end((explode('/', $url)));
       $url_end = preg_replace("/_/", " ", $url_end);
       echo '<h2><a href = "'.$url.'">'.$url_end.'</a></h2><br>';
      }
    }
    
    else
    {
     #echo $value.' : '."The query could not be searched!".'<br>';
    }
}     

?>


