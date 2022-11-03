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