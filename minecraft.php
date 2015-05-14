<?php echo "test";
$var = exec("/etc/init.d/minecraft status");
echo $var
?>
<br>
<a href="/minecraftstart.php" > Start </a> Marche pas<br>
<a href="/minecraftstop.php" >stop</a> Marche! M'envoyer un message si cliquer dessus pourque je redemarre le serveur ^^ <br>
<a href="/minecraftcommandtest.php" >Command</a>
<br>
<style>
#log {
    width: 100%;
    font-family: Consolas, monospace;
    background: black;
    color: gold;
    font-size: 90%;
    }
</style>
 
<?php
$log = file_get_contents('/home/minecraft/logs/latest.log');
//file_put_contents('latest.log', $log);        // distant/local
$log = explode("\n", $log);
//echo count($log).' lignes';
echo '<div id="log">';
 
foreach ($log as $l) {
    $ok = false;
    $l = htmlspecialchars($l);
    if (strstr($l, 'Can\'t keep up!') or strstr($l, 'lost connection:'))
        $l = '';
    elseif (strstr($l, '[Server thread/INFO]')) {
        $l = str_replace('[Server thread/INFO]', 'INFO ', $l);
        $ok = true;
        if (strstr($l, 'joined the game'))
            $l = '<span style="color:green">'.$l.'</span>';
        elseif (strstr($l, 'left the game'))
            $l = '<span style="color:red">'.$l.'</span>';
        elseif (strstr($l, 'logged in with entity') or strstr($l, 'User Authenticator') or strstr($l, 'Query Listener'))
            $l = '<span style="color:grey">'.$l.'</span>';
        elseif (strstr($l, '&lt;'))
            $l = '<span style="color:white">'.$l.'</span>';
        }
    elseif (strstr($l, '[Server thread/WARN]')) {
        $l = str_replace('[Server thread/WARN]', 'WARN ', $l);
        $ok = true;
        if (strstr($l, 'moved wrongly!'))
            $l = '<span style="color:grey">'.$l.'</span>'; 
        }
    elseif (strstr($l, 'User Authenticator') or strstr($l, 'Query Listener')) {
        $ok = true;
        $l = '<span style="color:grey">'.$l.'</span>'; 
        }
    else {
        $ok = true;
        }
    if ($ok == true)
        echo $l.'<br />';
    }
//print_r($log);
echo '</div>';
 
?>
