# EXIF - Metadata

`exiftool ` the file
And search the GPS Location on Google Maps

flag :``
Marseille
``

# Point à la ligne

From the name of the challenge, we make two assumptions:

- Match characters under dot (dot and next line)

- And vice versa (next line and point)

flag :``
chatelet15h
``

# Steganomobile

Use [dcode.fr/code-multitap-abc](https://www.dcode.fr/code-multitap-abc) for decoding 

flag :``
cellphone
``

# Twitter Secret Messages

Use [Twitter Secret Messages](https://holloway.nz/steg/) for decoding

flag :``
grand central terminal
``

# TXT - George et Alfred

When reading Alfred de Musset's answer, we notice a hint, which is to read the first word of each sentence. So we see that Alfred is addressing a question to George Sand, we use the same method and we find the flag

flag :``
Cette Nuit
``

# WAV - Analyse de bruit

Use the Audicity tool to modify the sound. After much testing, the formula for an English voiceover is: Speed ​​Low (reduced to 30%) + Reverse (reverse audio track)

flag :``
3b27641fc5h0
``

# Poem from Space

Use the Whitespace Language decoding tool to decode on site [dcode.fr/langage-whitespace](https://www.dcode.fr/langage-whitespace)

flag : ``
RootMe{Wh1t3_Sp4c3}
``

# Points jaunes

Use stegsolve, open the image, swicth in **Gray Bits**, you have a white square. Is the serial number of the scanner.

<img src="../files/StegSolve.png" alt="StegSolve" width="400px"/>

Make a table of each points of the image according to the bits and you will find the flag

<img src="../files/Yellow_Dot.png" alt="Yellow Dot" width="400px"/>

Or use [Docucolor Decoder](https://wiki.tcl-lang.org/page/Docucolor+yellow+tracking+dots+decoder) in TCL language

flag :``
11:05 27/07/2014 06922930
``