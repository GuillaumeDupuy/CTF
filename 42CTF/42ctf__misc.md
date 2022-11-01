## Dorkside
- google `"bill" https://cse.buffalo.edu/`, click in the site `Index of /~rapaport/584/S10` & find `rapaport.txt`
or 
- google `cse.buffalo.edu password 2007`, click in the site `20070202-password.txt`
or 
- google `cse.buffalo.edu password 2007`, click in the site `20070121-howtoaccessreadings.txt`

<details>
<summary markdown="span">Answer</summary>

flag : ``
Rapaport
``
</details>

## Norminet
- existfool `Image Description`
- pastebin, search `xn` and click
    - instagram pseudo
    - twitter search `(from:42norminet)`
    - job at school in the badge
- camelCase

<details>
<summary markdown="span">Answer</summary>

flag : ``
020317-42norminet-executiveCat
``
</details>

## Force brute
[python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/42CTF/scripts/force_brute.py)

```sh
$ python3 force_brute.py > text.txt
$ cat text.txt | grep 55d91e
. . .
55d91e34650fd1a804cd94f5f39b34fb _
. . .
```
<details>
<summary markdown="span">Answer</summary>

flag : ``
21Iliad18Elisa
``
</details>

## Smiley

In Progress

<!-- ```sh
$ ./smiley
$ 42CTF{}
$ could you give me a hint please??
```
```
xxd ./smiley | head
``` -->