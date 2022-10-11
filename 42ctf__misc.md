## Dorkside
- google `"bill" https://cse.buffalo.edu/`, click in the site `Index of /~rapaport/584/S10` & find `rapaport.txt`
or 
- google `cse.buffalo.edu password 2007`, click in the site `20070202-password.txt`
or 
- google `cse.buffalo.edu password 2007`, click in the site `20070121-howtoaccessreadings.txt`

flag : ``
Rapaport
``

## Norminet
- existfool `Image Description`
- pastebin, search `xn` and click
- twitter search `(from:42norminet)`

```
The first part is the date of my first tweet.
==> March 2, 2017
Follows my instagram handle...
==> 42norminet
Then to finish my status within the school 42
(noted on my map 42)!
==> Executive Cat
```
- camelCase

flag : ``
Exemple :
42CTF{271219-pseudoInstagram-posteALecole}
Flag :
42CTF{020317-42norminet-ExecutiveCat}
``

## Force brute
[python](https://github.com/GuillaumeDupuy/42CTF/blob/main/scripts/ft_force_brute.py)

```sh
$ python3 ft_force_brute.py > text.txt
$ cat text.txt | grep 55d91e
. . .
55d91e34650fd1a804cd94f5f39b34fb _
. . .
```
flag : ``
21Iliad18Elisa
``

## smiley
```scala
$ file _
$ strings _
$ nm _
$ objdump -p _
$ xxd ./smiley | head
```
