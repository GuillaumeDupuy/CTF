# Reverse Polarity

Use [CyberChef](https://gchq.github.io/CyberChef/) from Binary

<details>

<summary markdown="span">Answer</summary>

flag :``
CTF{Bit_Flippin}
``
</details>

# Morse Code

Use [CyberChef](https://gchq.github.io/CyberChef/) from Morse Code

<details>

<summary markdown="span">Answer</summary>

flag :``
FLAGSAMUELMORSEISCOOLBYTHEWAYILIKECHEES
``
</details>

# Base 2 2 the 6

Use [CyberChef](https://gchq.github.io/CyberChef/) from Base64

<details>

<summary markdown="span">Answer</summary>

flag :``
CTF{FlaggyWaggyRaggy}
``
</details>

# Character Encoding

Use [CyberChef](https://gchq.github.io/CyberChef/) from Hex

<details>

<summary markdown="span">Answer</summary>

flag :``
ABCTF{45C11_15_U53FUL}
``
</details>

# Vigenere Cipher

Use [Cryptii](https://cryptii.com/pipes/vigenere-cipher) with the key : blorpy

<details>

<summary markdown="span">Answer</summary>

flag :``
flag{CiphersAreAwesome}
``
</details>

# BruXOR

Use [Dcode](https://www.dcode.fr/chiffre-xor) XOR

<details>

<summary markdown="span">Answer</summary>

flag :``
flag{y0u_Have_bruteforce_XOR}
``
</details>

# HyperStream Test #2

Use [CyberChef](https://gchq.github.io/CyberChef/) from Bacon Cipher Decode with Standard Alphabet

<details>

<summary markdown="span">Answer</summary>

flag :``
ILOUEBACONDONTYOU
``
</details>

# RSA Noob

Use [Dcode](https://www.dcode.fr/chiffre-rsa) RSA

<details>

<summary markdown="span">Answer</summary>

flag :``
abctf{b3tter_up_y0ur_e}
``
</details>

# Substitution Cipher

Use [Dcode](https://www.dcode.fr/monoalphabetic-substitution) Mono-Alphabetic Substitution Cipher

<details>

<summary markdown="span">Answer</summary>

flag :``
IFONLYMODERNCRYPTOWASLIKETHIS
``
</details>

# Substitution Cipher

``python
print(hex(0xc4115 ^ 0x4cf8))
``

<details>

<summary markdown="span">Answer</summary>

flag :``
0xc0ded
``
</details>

# Modern Gaius Julius Caesar 

The hint given by the title is Julius Ceaser, which is a rotatory cipher. The next hint is the keyboard. Yes, the challenge only works for the US keyboard. As you guessed, the first three letters should be ‘CTF’ where we have : B -> C, U -> T, H -> F

<img src="../files/US_Keyboard.png" alt="US_Keyboard" width="400px"/>

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Cyb3r_Cae54r}
``
</details>

# Modern Gaius Julius Caesar 

Use [Dcode](https://www.dcode.fr/polybius-cipher) Polybius Cipher with the alphabet encryption grid excluding the letter k

<details>

<summary markdown="span">Answer</summary>

flag :``
CTF{THUMBS_UP}
``
</details>

# Suspecious message

Use [Playfair Cipher](https://www.boxentriq.com/code-breaking/playfair-cipher) to decode with the encryption key in the image png

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFLEARN{PL4YF41R_1S_C00L_C1PHERRRR}
``
</details>

# So many 64s

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/64s.py) for recover flag

<details>

<summary markdown="span">Answer</summary>

flag :``
ABCTF{pr3tty_b4s1c_r1ght?}
``
</details>

# RSA Beginner

Use [Dcode](https://www.dcode.fr/chiffre-rsa) RSA

<details>

<summary markdown="span">Answer</summary>

flag :``
abctf{rs4_is_aw3s0m3}
``
</details>

# RSA Twins!

Use [Dcode](https://www.dcode.fr/chiffre-rsa) RSA

<details>

<summary markdown="span">Answer</summary>

flag :``
flag{i_l0v3_tw1N_pr1m3s}
``
</details>

# CoppeRSA Lattice

Use [Dcode](https://www.dcode.fr/chiffre-rsa) RSA

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{n0t_th4t_s3cur3_4ft3r_4ll}
``
</details>

# Encryption Master 

Just use fourth time [Cyberchef](https://gchq.github.io/CyberChef/) from Base64 from Hex from Binary from base64

<details>

<summary markdown="span">Answer</summary>

flag :``
CTF{I_AM_PROUD_OF_YOU}
``
</details>

# Tone dialing

We have a wav file. Open it, the sound is like when pressing phone numbers. So, use [Dtmf](https://unframework.github.io/dtmf-detect/#/) tool to recover the number : ``67847010810197110123678289808479718265807289125``. Change the string number to text and you have the flag

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlean{CRYPTOGRAPHY}
``
</details>

# ALEXCTF CR2: Many time secrets

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/cribdrag.py)

We know that part of the key is ALEXCTF{ is a good start. We will get a lot of possibilities for plain text , We need to make a calculate guess of the each line. After a little work we can get the full key that reused again and again.

<details>

<summary markdown="span">Answer</summary>

flag :``
ALEXCTF{HERE_GOES_THE_KEY}
``
</details>

# ALEXCTF CR2: Many time secrets

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/symbdec.py)

And you can see this is encoded in decimal. To decode this use [Cyberchef](https://gchq.github.io/CyberChef/) from Decimal

<details>

<summary markdown="span">Answer</summary>

flag :``
CTF{Star_._Wars_._For_._Life}
``
</details>

# The Simpsons

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/simpsons.py)

You can see, the string encoded is ``jrjerwhzkrexar`` and the content of the key is ``How much did Maggie originally cost? (Divided by 8, to the nearest integer, and then plus four)``

So it's a hint, what's the price of Maggie ? Google knows everything, the price is *847,63 $*

Now let's go follow the hint : 

``847,63 / 8 = 105,95``

We take the nearest integer:

``106``

We add 4:

``106+4=110``

But don't forget that we had a chr() around the solution, so:

``chr(110) = 'n'``

As we know key='n', let's move on. I copied the line as it was in python and run:

``python
key = key + key + chr(ord(key)-4)
key = 'nnj'
``

Now, you know :

``encoded = "jrjerwhzkrexar"
key = "nnj"``

Use [Dcode](https://www.dcode.fr/vigenere-cipher) Vigenere Cipher 

<details>

<summary markdown="span">Answer</summary>

flag :``
wearenumberone
``
</details>

# XOR Is Friend Not Food

You have to find out the key to decode this XOR encryption : ``091b1100160b1d19170b051d280500351b1f092c0d00181c0e``, I use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/cribdrag.py) to get the key.

I saw at index 0 there were words that made sense, namely **jowls**, I thought that it was a key, so use [Dcode](https://www.dcode.fr/xor-cipher)

<details>

<summary markdown="span">Answer</summary>

flag :``
ctflearn{xor_is_the_goop}
``
</details>

# Linear-feedback. Shift. Register.

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/linearfeed.py)

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{Lin34r_F33db4ck_Sh1fT_R3g1st3r}
``
</details>

# We want Nudes instead of Nukes

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/nukes.py)

<details>

<summary markdown="span">Answer</summary>

flag :``
flag{2c1289a05847cfd65ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}
``
</details>

# Polycrypto

It just converting given polynomial function to binary which is : `110011001101100011000010110011101111011011100000011000001101100011110010110111001101111011011010011000101100001011011000111001101011111001101000111001000110011010111110110101100110000001100000110110001111101`

After converting this binary to hexadecimal following hex string was obtained : `666C61677B70306C796E6F6D31616C735F3472335F6B30306C7D`

After converting this hex to ascii the flag was retrieved. 

<details>

<summary markdown="span">Answer</summary>

flag :``
flag{p0lynom1als_4r3_k00l}
``
</details>

# Skynet Is (Almost) Taking Over

I factorize `n1` through [Factorize](http://factordb.com/) and got `p1` and `q1`

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/skynet.py)

<details>

<summary markdown="span">Answer</summary>

flag :``
flag{will_he_be_back}
``
</details>

# Image Editing

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/img.py)

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{1_kn3W_tH3_r3D_w4s_0ff}
``
</details>

# The Safest Encryption

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/xor.py)

``python
python xor.py CTFlearn.pdf CTFlearn.txt output.pdf
``

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{CTFlearn_is_fun_hope_you_enjoyed_it!}
``
</details>

# Zippy.zip

Use [python scripts](https://github.com/GuillaumeDupuy/CTF/blob/main/CTFLearn/scripts/zip.py) on Python2

``python
python2 zip.py
``

<details>

<summary markdown="span">Answer</summary>

flag :``
CTFlearn{s0m3t1m35_u$1ng_h4rd_p4s5w0rd_i5_n0t_3n0ugh}
``
</details>