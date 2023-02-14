# unzip to file ./zippy directory
import binascii
import base64
import string
import itertools
import struct

alph = '}abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/={_-!@#$%^&*()><? '

crcdict = {}

print("computing all possible CRCs...")

for x in itertools.product(list(alph), repeat=4):
    st = ''.join(x)
    testcrc = binascii.crc32(st)
    crcdict[struct.pack('<i', testcrc)] = st

print("Done!")

for i in range(14):

    f = open("flag{}.zip".format(i))
    data = f.read()
    f.close()
    crc = ''.join(data[14:18])
    
    if crc in crcdict:
        print(crcdict[crc])
    else:
        print("FAILED!")