## Dorkside
- google `"bill" https://cse.buffalo.edu/` & find `howtoaccessreadings.txt`

## Norminet
- pastebin `xn`
- twitter search `(from:42norminet) until:2017-03-10 since:2017-02-01`
- camelCase

## Force brute
[python](https://github.com/GuillaumeDupuy/42CTF/blob/main/scripts/ft_force_brute.py)
```py
import hashlib

#comp = ['free', 'iliad', '42', 'mediawan', 'scaleway']
#name = ['delphine', 'elisa', 'michel', 'camille', 'john', 'jules']

comp = ['Free', 'Iliad', '42', 'Mediawan', 'Scaleway']
name = ['Delphine', 'Elisa', 'Michel', 'Camille', 'John', 'Jules']

for i in range(43):
    for r in range(1, 51):
        for c in comp:
            for n in name:
                s = str(i) + c + str(r) + n
                res = hashlib.md5(s.encode())
                print(s, res.hexdigest())
```
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
