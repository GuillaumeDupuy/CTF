expected = [0] * 26
expected[0] = ord('W')
expected[1] = 0x42
expected[2] = 0x4b
expected[3] = 0x45
expected[4] = 0xcc
expected[5] = 0xbb
expected[6] = 0x81
expected[7] = 0xcc
expected[8] = 0x71
expected[9] = 0x7a
expected[10] = 0x71
expected[11] = 0x66
expected[12] = 0xdf
expected[13] = 0xbb
expected[14] = 0x86
expected[15] = 0xcd
expected[16] = 100
expected[17] = 0x6f
expected[18] = 0x6e
expected[19] = 0x5c
expected[20] = 0xf2
expected[21] = 0xad
expected[22] = 0x9a
expected[23] = 0xd8
expected[24] = 0x7e
expected[25] = 0x6f

def unshuffle(param):
    buf = [0] * len(param)

    for i in range(0, len(param)-1, 2):
        buf[i+1] = param[i]

    for i in range(1, len(param), 2):
        buf[i-1] = param[i]

    return buf

def decrypt(block):
    local_48 = [1,3,3,7, 0xde, 0xad, 0xbe, 0xef]
    buf = [0] * len(block)
    ind = 0

    for i in range(len(block)):
        buf[i] = block[i] ^ local_48[ind]
        ind = (ind+1)%len(local_48)
    return buf

def backward():
    buf = unshuffle(expected)
    buf = decrypt(buf)
    print(''.join(map(chr, buf)))

backward()