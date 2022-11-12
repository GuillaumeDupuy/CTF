import string
data = [0]*21

data[0] = 0x13693
data[1] = 0x6b2c0
data[2] = 0x11a9f9 
data[3] = 0x157000 
data[4] = 0x1cb91 
data[5] = 0x1bb528 
data[6] = 0x1bb528 
data[7] = 0xded21 
data[8] = 0x144f38
data[9] = 0xfb89d
data[10] = 0x169b48 
data[11] = 0xd151f 
data[12] = 0x8b98b
data[13] = 0x17d140
data[14] = 0xded21 
data[15] = 0x1338c0 
data[16] = 0x1338c0
data[17] = 0x11a9f9
data[18] = 0x1b000 
data[19] = 0x144f38 
data[20] = 0x1734eb  

flag = "CTFlearn{"

candidates = string.ascii_uppercase+string.ascii_lowercase+string.digits+'+'+'_'+'-'

for i in range(len(data)):
    for j in candidates:
        if pow(ord(j),3) == data[i]:
            flag += j
            break

print(flag+'}')