## We need a pattern
letter frequency in english
```erlang
╝±╩ ¥║£║ ╗═ ┴±╔£ ¤╬╣╦:

. . .
# First hint
┼ ¿ ¤
c t f

# Frequency
║: 1095
¿: 874
±: 704
╣: 683
¥: 594
╗: 569
╝: 566
═: 512
£: 458
╬: 422
®: 390
╔: 254
╩: 252
╦: 203
¤: 192
,: 179
┼: 175
┴: 168
©: 145
█: 139
Ø: 133
≡: 96
×: 68
': 66
↵: 51
.: 45
```

42┼¿¤{®±_╝±¿_╔═║_©±╝±╣╬Ø¥╣█║¿╗┼_═╔█═¿╗¿╔¿╗±╝}
⚠️ UpperCase

<details>
<summary markdown="span">Answer</summary>

flag : ``
do_not_use_monoalphabetic_substitution
``
</details>

## Vous n'avez pas les bases
- use [gchq](http://gchq.github.io/CyberChef)
  - Recipe From Base64, From Base32 and From Hex

<details>
<summary markdown="span">Answer</summary>

flag : ``
you're_ready_for_the_real_world
``
</details>

## Very Short Crypto

[shell scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/42CTF/scripts/find_rsa.sh)

Now go to the dcode site and enter the value of C.txt on the first, enter the value of N.txt in the third and click on Calculate/Decrypt. (if Public Key E is empty, enter the default : 65537)

###### then decode using E (Small E attack) [Dcode](https://www.dcode.fr/rsa-cipher)

<details>
<summary markdown="span">Answer</summary>

flag : ``
thisMessageIsDefinitely2short2BeSecure
``
</details>