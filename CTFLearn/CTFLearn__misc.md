# Where Can My Robot Go ?

You have to go to the root of the page, go to the url and put ``/robots.txt`` then go to the page written in the file : ``/70r3hnanldfspufdsoifnlds.html``

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{r0b0ts_4r3_th3_futur3}
``
</details>

# Practice Flag

Just copy and paste

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{4m_1_4_r3al_h4ck3r_y3t}
``
</details>

# Wikipedia

Search on [Wikipedia](https://www.wikipedia.org/) the `128.125.52.138` and you see a modification of the page 

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{4m_1_4_r3al_h4ck3r_y3t}
``
</details>

# QR Code

Scan the QR Code, recover the string encoded on base64, convert with [Cyberchef](https://gchq.github.io/CyberChef/), recover the string 

<details>

<summary markdown="span">Answer</summary>

flag :``
n0_body_f0rget_qr_code
``
</details>

# Time Traveller

Use [Wayback Machine](https://web.archive.org/), search ``nasa.gov`` website, select the date of `december` and recover the email of nasa

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{today@nasa.gov}
``
</details>

# What could this be?

This is JSFuck, so let's go use a tool to decode [Dcode](https://www.dcode.fr/jsfuck-language)

<details>

<summary markdown="span">Answer</summary>

flag :``
flag{5uch_j4v4_5crip7_much_w0w
``
</details>

# Rock Paper Scissors

Just copy and paste the commande and beat the bot 10 times with this order : `PRPSPPSPRP`

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{r0ck_p4per_skiss0rs}
``
</details>

# Ambush Mission

Use `stegsolve` or [Stegonline](https://stegonline.georgeom.net/upload), select `red plane 0` and you see a string base64.
So use [Cyberchef](https://gchq.github.io/CyberChef/), reverse the string and convert from base64

<details>

<summary markdown="span">Answer</summary>

flag :``
m3Et_me_4t_12_aM
``
</details>

# Help Bity

Use [Cyberchef](https://gchq.github.io/CyberChef/) from Magic

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFLern{b1nry_1s_awes0me}
``
</details>

# My Friend John

We can open [`MyFriendJohn.zip`](./MyFriendJohn.zip) using [7zip](https://www.7-zip.org/) and extract `use-rockyou.zip`.

Now we need a password to open `use-rockyou.zip`. There's a really popular wordlist called rockyou which can be downloaded [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt).

We can use [fcrackzip](https://github.com/hyc/fcrackzip)'s dictionary attack: `fcrackzip -v -u -D -p rockyou.txt use-rockyou.zip` using rockyou.

We now see `custom-list.txt` and `custom-list.zip`. We can use the custom word list to unlock the the zip file: `fcrackzip -v -u -D -p custom-list.txt custom-list.zip`.

The last zip file is called `brute-force-pin.zip`. A pin is usually between 4 and 6 numeric digits. `fcrackzip -b -c "1" -l 4-6 -v -u brute-force-pin.zip`. The `-c "1"` means only use numeric digits when bruteforcing.

Finally we get a `flag.txt`

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{s0_n0W_y0uv3_M3t_J0hN}
``
</details>

# F1L3 M1X3R

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/hexdump.py) to rearrange the bytes of the flag

<details>

<summary markdown="span">Answer</summary>

flag :``
Flag{byt3_sw4p}
``
</details>

# Rock Paper Scissors 2

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/RockPaperScissors2.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{m3rs3nn3_kind4_c00l}
``
</details>

# Combo Safe-box

The most important slide is number 6, because slide 6 goes to pass or fail

```
10 = 7
3 = 5
13 = 1
5 = 6
8 = 2
6 = 3
```

<details>
<summary markdown="span">Answer</summary>

flag :``
751623
``
</details>

# Get Into Command Mission

Use `strings`, recover the output : 

```
data:image/png;base64,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
```

And use [Base64 to PNG](https://base64.guru/converter/decode/image/png) to discover the flag

<details>
<summary markdown="span">Answer</summary>

flag :``
Arm0uR_pPTi4
``
</details>

# Flag Protocol

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/protocol.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{y0u_c4ptur3d_m3}
``
</details>

# Android, run!

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/android.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
FLAG{Ch4ll4ng3-5UcC33D3d-c0nt1nUe!}
``
</details>