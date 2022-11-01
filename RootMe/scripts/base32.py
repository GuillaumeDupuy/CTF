import base64 as b64
import math
from tinyscript import *

DEF_BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
DEF_BASE32 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

def unhide_bits(encoded, charset, pad="=", n_pad=8):
    def __gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
    padding = encoded.count(b(pad))
    n_repr = int(math.ceil(math.log(len(charset), 2)))
    w_len  = n_repr * n_pad / __gcd(n_repr, n_pad)
    n_char = int(math.ceil(float(w_len) / n_repr))
    if encoded == "" or len(encoded) % n_char != 0 or padding == 0:
        return
    unused = {n: int(w_len - n * n_repr) % n_pad for n in range(n_char)}
    b_val  = bin(b(charset).index(encoded.rstrip(b(pad))[-1]))[2:].zfill(n_repr)
    return b(b_val[-unused[padding]:])

filename = "ch15.txt"
f = open(filename,"r")
txtstr = f.read()
f.close()
txtstr = txtstr.split("Native")[0].split("Comment")[-1].split("\n")[0].split(":")[1]

b64arr = txtstr.split(".")
asciiarr1 = []
asciiarr2 = []

for val in b64arr:
    asciiarr1.append(b64.b64decode(val).decode())
    
asciistr = "".join(asciiarr1)

f = open("ch15decoded.txt","w")
f.write(asciistr)
f.close()

bitstr = b""

for val in b64arr:
    bitstr += unhide_bits(val.encode(),charset=DEF_BASE64) or b("")

b32str = b("").join(ts.bin2str(bitstr[i:i+8]) for i in range(0, len(bitstr), 8))
b32arr = b32str.strip(b"\x00").decode().split("\n")

bitstr = b""
for val in b32arr:
    bitstr += unhide_bits(val.encode(),charset=DEF_BASE32) or b("")

asciistr = b("").join(ts.bin2str(bitstr[i:i+8]) for i in range(0, len(bitstr), 8))
asciistr = asciistr.strip(b"\x00").decode()

print(asciistr)