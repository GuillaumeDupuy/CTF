def bytes_to_array(dat, sz):
    dat = dat.split()
    arr = []
    for i in range(0, len(dat), sz):
        arr.append(int(''.join(reversed(dat[i:i+sz])), 16))
    return arr

msg5 = "21 7e 3d 2a 38 12 1b 1f 0c 10 05 2c 0b 16 0c 18 1b 0d 0a 0d 0e 17 1b 12 1b 21 38 1b 0d 0a 17 08 1f 12 03"
msg5 = bytes_to_array(msg5, 1)

def uncheck():
    buf = [0]*msg5[0]

    if msg5[0] != 0:
        for i in range(msg5[0]):
            buf[i] = msg5[i+2] ^ msg5[1]
    return buf


buf = uncheck()
print(''.join(map(chr, buf)))