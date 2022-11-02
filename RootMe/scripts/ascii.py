flag = ""

for i in range(1,14):
    
    if i < 10: 
        i = "0" + str(i)

    f = open("ch21" + str(i) + ".txt")
    flag += chr(int(f.read().split("/")[0].split("=")[1]))

print(flag)

# from apng import parse_chunks
 
# img = open("ch21.apng", 'rb').read()
# chunks = parse_chunks(img)

# fctl_chunks = []
# [fctl_chunks.append(c) for c in chunks if c[0] == 'fcTL']

# print(''.join([chr(int(c[1][28:30].hex(), 16)) for c in fctl_chunks]))