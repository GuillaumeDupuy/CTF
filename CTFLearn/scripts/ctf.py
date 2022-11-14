flag = [
	0x4B , 0x5C , 0x4E , 0x64 , 0x6D , 0x69 , 0x7A , 0x66 ,
	0x73 , 0x60 , 0x38 , 0x65 , 0x3B , 0x57 , 0x6B , 0x38 ,
	0x65 , 0x78 , 0x7D , 0x7C , 0x3B , 0x7A , 0x57 , 0x7A ,
	0x3B , 0x7E , 0x38 , 0x64 , 0x7D , 0x7C , 0x39 , 0x38 ,
	0x66 , 0x75
]

res = ""

def checkCharacter(c):
    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@{}()-"
    if c in character:
        return True
    else: return False

for i in range(100):

    isOk = True

    for x in range(len(flag)):
        charac = str(chr(flag[x] - i))
        res += charac

    if isOk == True:
        if "CTF" in res:

            print(str(i) + ". " + res)

            for x in flag:
                res += chr(x ^ 8)

            res = res.split("^m")[1]

            res = res.replace("{","[")
            res = res.replace("}","]")
            res = res.replace("h","H")

            print(res)

            break
    res = ""