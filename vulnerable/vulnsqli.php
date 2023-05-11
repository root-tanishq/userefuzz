<?php 
// I am using cheap trick to run mysql on it 
// due to of some issues my xampp is not working perfectly

echo "UseReFuzz Tool testing template";
$ufzParam = $_SERVER['HTTP_USER_AGENT'];
echo "<br/>Payload => $ufzParam";
exec("/opt/lampp/bin/mysql -u root -proot -D mysql -e 'select * from db where Db =\"$ufzParam\";'");

/* Request
GET /userefuzz.php HTTP/1.1
Host: 192.168.1.11:8000
Upgrade-Insecure-Requests: 1
User-Agent: test";SELECT SLEEP(5);-- -
Connection: close
*/

?>
