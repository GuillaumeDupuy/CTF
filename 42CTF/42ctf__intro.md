# Ancient Crypto
```sh
# ROT10

$ wget _
$ cat ancient_crypto.txt | tr 'k-za-jK-ZA-J' 'a-zA-Z'
```

flag : ``
EASY_TO_BRUTE_FORCE
``

# My Little Pwn
```sh
$ wget _
$ tar zxvf _

python3 -c "print('A' * 64 + 'B')" | nc challenges.42ctf.org 3002
```

- what does `-zxvf` mean
  - z means (un)z̲ip
  - x means ex̲tract
  - v means print filenames v̲erbose
  - f means the following argument is a f̱ilename.

flag : ``
you_re_ready_for_the_real_pwn
``

# Client Side
- inspect & enable checkbox

flag : ``
html_is_too_easy_for_you
``

# It's all here
- `exiftool _`

flag : ``
metada_has_no_secrets_for_you
``