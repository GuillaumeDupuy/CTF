# Basic Android RE 1

Decode the APK file with `apktool`

``sh
apktool -v decode BasicAndroidRE1.apk
``

Now check all the files in the directory decode and you see a three `const string` in the `MainActivity.smali` file
it's the flag but it's in three parts but one of the parts is encoded in [MD5 Decode](https://md5.gromweb.com/)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Spring2019_is_not_secure!}
``
</details>

# Pin

Use `ghidra`to reverse the bin, you can see that the input is checked against another variable stored in the `cek` function and the stored variable is a hex number. So convert `0x51615` in [Hex to Decimal](https://www.rapidtables.com/convert/number/hex-to-decimal.html)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{333333}
``
</details>

# Reykjavik

Using gdb -q Rejkjavik, we get can hop on to the main function using break points. The command for the same would be b * main. After reaching, using ni Next Instriction, we land up to the flag as mentioned below.

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Eye_L0ve_Iceland_U}
``
</details>

# Time to eat 

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/time.py)

Recover the output and execute

``python
python eat.py <<< 341eat009
``

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{ eaten_341eat009 }
``
</details>

# Rangoon

<details>
<summary markdown="span">Full explanation</summary>

[here](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/explanation_rangoon.md)
</details>

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Princess_Maha_Devi}
``
</details>

# RE_verseDIS

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/password.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
AbCTF{r3vers1ng_dud3}
``
</details>

# PyDis 

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/pydis.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Python_Reversing_Is_Pretty_Easy}
``
</details>

# Ramada

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/ramada.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{+Lip1zzaner_Stalli0ns}
``
</details>

# Jumper

<details>
<summary markdown="span">Full explanation</summary>

[here](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/explanation_jumper.md)
</details>

<details>
<summary markdown="span">Answer</summary>

flag :``
0x6d7592
``
</details>

# Raspberry

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/raspeberry.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{+Fruit123}AAAAAAAAAAAAA
``
</details>

# Recklinghausen

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/reck.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Ruhrfestspiele_Festival}
``
</details>

# Reverse Me

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/reverse.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFLearn{reversing_is_fun}
``
</details>

# Every Bit Counts

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/bit.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{w0w_you_f0und_My_fl@g_y0u_Ar3_so_much_n1c3}
``
</details>

# Rotterdam Reversing Challenge

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/rotterdam.py)

<details>
<summary markdown="span">Answer</summary>

flag :``
Rotterda_P0rt_Rh1ne_Bl1tz_W1tte
``
</details>

# Bite-code

Use [java scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/bit.java)

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{-1352854872}
``
</details>