# Forensics 101

Use ``strings``

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{wow!_data_is_cool}
``
</details>

# Taking LS

Cat the file ``ThePassword.txt`` to recover the password of pdf file 

<details>
<summary markdown="span">Answer</summary>

flag :``
ABCTF{T3Rm1n4l_is_C00l}
``
</details>

# Binwalk

Use binwalk extract to recover the png file with the file

<details>
<summary markdown="span">Answer</summary>

flag :``
ABCTF{b1nw4lk_is_us3ful}
``
</details>

# WOW.... So Meta

`exiftool ` the file

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{EEe_x_I_FFf}
``
</details>

# 07601

Use `strings` the file

<details>
<summary markdown="span">Answer</summary>

flag :``
ABCTF{Du$t1nS_D0jo}
``
</details>

# Git Is Good

Use git command

``sh
git log -p
``

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{protect_your_git}
``
</details>

# Exif

Use `exiftool` the file

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{3l1t3_3x1f_4uth0r1ty_dud3br0}
``
</details>

# Rubber Duck

Use `exiftool` the file

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{ILoveJakarta}
``
</details>

# Snowboard

Use ``strings`` file, select the strings in base64 and convert into string

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{SkiBanff}
``
</details>

# PikesPeak

Use ``strings`` and test all flag

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Gandalf}
``
</details>

# I'm a dump

Use ``strings`` file

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{fl4ggyfl4g}
</details>

# Chalkboard

Use ``strings``, recover the flag and calculate x and y and replace

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{I_Like_Math_2_5}
``
</details>

# Tux!

Use ``strings`` file, select the strings in base64 and convert into string. You have a password
Use binwalk to extract and use the password for open the file of the flag

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Linux_Is_Awesome}
``
</details>

# A CAPture of a Flag 

Use wireshark

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{AFlaginPCAP}
``
</details>

# Milk's Best Friend

Use binwalk to extract png file and use ``strings`` on the png extracted

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{eat_more_oreos}
``
</details>

# Up For A Little Challenge?

Use ``strings`` and click on the link, download the file, ls th folder and zip the secret file. Use the password on the first string to open the jpg and check on the bottom right on the image

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{hack_complete}
``
</details>

# Digital Camouflage

Use wireshark

<details>
<summary markdown="span">Answer</summary>

flag :``
PApdsjRTae
``
</details>

# Naughty Cat

Use binwalk to extract the rar and mp3 file. Open the rar with [Hexed](https://hexed.it/) to repair the error file and replace the signature file. Now use Audacity and select spectogramme to see the password of the txt file in the rar. Recover the encoded string in base64 and convert to recover the flag

<details>
<summary markdown="span">Answer</summary>

flag :``
f0r3n51cs_ma5t3r
``
</details>

# MountainMan

Use [Hexed](https://hexed.it/), search ``ff d9``, copy the hex between the two delimeter and use [Cyberchef](https://gchq.github.io/CyberChef/) from Hex and Magic to recover the flag by XOR

<details>
<summary markdown="span">Answer</summary>

flag :``
CTF{Ubuntu_r0ck5}
``
</details>

# Corrupted File

Use [Hexed](https://hexed.it/), replace the signature file by the signature of GIF file : ``47 49 46 38``
Recover the fragment of encode string in base64 : ``ZmxhZ3tnMWZfb3JfajFmfQ==`` and convert

You can use the command to convert each frame of the gif to png, to see properly each fragment

``sh
convert -coalesce unopenable.gif target.png
``

<details>
<summary markdown="span">Answer</summary>

flag :``
flag{glf_or_jlf}
``
</details>

# Pho Is Tasty!

Use hex editor to analyse the image [Hexed](https://hexed.it/) and copy the hex code till the flag we can see on the side. Convert hex into ascii. Remove the ``.`` in between from the converted string and we will have our flag.

<details>
<summary markdown="span">Answer</summary>

flag :``
CTFlearn{I_Love_Pho!!!}
``
</details>
