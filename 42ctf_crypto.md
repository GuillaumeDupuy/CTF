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
flag : `
42ctf{do_not_use_monoalphabetic_substitution}
`

## Vous n'avez pas les bases
- use [gchq](http://gchq.github.io/CyberChef)
  - Recipe From Base64, From Base32 and From Hex

flag : `
you're_ready_for_the_real_world
`


## Very Short Crypto
```sh
#!/bin/bash

openssl rsa -noout -text -inform PEM -in pub.pem -pubin > pubkey
cat pubkey | sed -e 's/^Pub.*//' -e 's/^Mod.*//' -e 's/Exp.*//' -e 's/://g' -e 's/ //g' > temp
tr -d '\n' < temp > N
cat pubkey && echo ""
rm temp

cat N && echo "\n- modulus edited\n"

cat N | xargs python -c "import sys; print(int(str(sys.argv[1]), 16))"
echo "- public key value (integer) n\n"

cat ciphertext | xargs python -c "import sys; print(int(str(sys.argv[1]), 16))"
echo "- ciphertext value (integer) c"
```
###### then decode using E (Small E attack) [dcode.fr/rsa-cipher](https://www.dcode.fr/rsa-cipher)
—\
[shell script](https://github.com/nuoxoxo/writeups/blob/main/scripts/ft_very_short_crypto.sh)
