file = open("TheMessage.txt", "r", encoding="utf8").read()

res = ""

for ch in file:

	if ord(ch) == 32:
		res += "0"
	else:
		res += "1"

txt = open("flag.txt", "w")
txt.write(res)
txt.close()