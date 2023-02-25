target = "W8Hj?1VESL^g4xwcvtW%humtEosd$Fq^dXPvi$#sSEe@o618Zl9.5PFrvC%O_E*LB%Igl8qur9SuLAp4MkK#pRzwJHI*Fn9mUs%mGK^RQKO.G*JFJvV%?VJpCpVF9eJuz5&kB!&_VF5DrF?U?jfm&x^9aC7X2(&cGGzbLbOsSOuBeq*ZT%fpc&9riTDO5X%RuTKI@vCqu#CsTAp$Q9WoXJv96.ySdB2EfMK*$NX?.U*aDrfPQQPhFB9cC6y0hMGvbgjBogSux65gTL#Cm9TQt7nTayu9Vr%thh2GnnikE8JnIwlHfreZep^sZ6IrnXT#qu50Lv.Rd_XPDfgwzWcJ3ISjKM!ftRllVyF$?RE_dcJT5&uKZJ!WsqR853uLzcs!8&VyRuTDsiq#6PdmBNlPI$tPi?wZ5$ACCf9yda!OkP.Dc73Nx.Nt1Rj0O.?P!sZDB^d0LN1qXR31!t?OZ#mm7SfZHPO*4gx1J0nyC^d2EKeq^f4h7mSqaIcMv0ZT@G0M"

kernelenc1 = []
kernelenc2 = []

for i in range(len(target)):
	kernelenc1.append(ord(target[i]))
	kernelenc2.append(ord(target[i]))


#n % 2^i = n & (2^i - 1)

v21val = 0xBAADF00D
v22val = 0xBAADF010
v23val = 0xBAADF013
v24val = 0xBAADF016
v25val = 0xBAADF019
v26val = 0xBAADF01C
v27val = 0xBAADF01F
v28val = 0xBAADF022
v29val = 0xBAADF025
v30val = 0xBAADF028 

o = "CTFlearn{"

char1 = 0 #Đếm xem mình đã có kí tự thứ 1 hay chưa, có thì mới ktra kí tự tiếp theo
char2 = 0
char3 = 0
char4 = 0
char5 = 0
char6 = 0
char7 = 0
char8 = 0
char9 = 0
char10 = 0

count = 0

for i in range (len(target)):
	if(char1 == 0 and kernelenc1[i] == kernelenc2[v21val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i]) % 512]):
			char1 += 1
			o += target[i]
for i in range (len(target)):
	if(char1 == 1 and char2 == 0 and kernelenc1[i] == kernelenc2[v22val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i]  + 3 ) % 512]):
			char2 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 0 and kernelenc1[i] == kernelenc2[v23val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 6) % 512]):
			char3 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 0 and kernelenc1[i] == kernelenc2[v24val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 9) % 512]):
			char4 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 0 and kernelenc1[i] == kernelenc2[v25val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 12) % 512]):
			char5 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 0 and kernelenc1[i] == kernelenc2[v26val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 15) % 512]):
			char6 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 1 and char7 == 0 and kernelenc1[i] == kernelenc2[v27val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 18) % 512]):
			char7 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 1 and char7 == 1 and char8 == 0 and kernelenc1[i] == kernelenc2[v28val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 21) % 512]):
			char8 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 1 and char7 == 1 and char8 == 1 and char9 == 0 and kernelenc1[i] == kernelenc2[v29val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 24) % 512]):
			char9 += 1
			o += target[i]
			break
for i in range (len(target)):
	if(char1 == 1 and char2 == 1 and char3 == 1 and char4 == 1 and char5 == 1 and char6 == 1 and char7 == 1 and char8 == 1 and char9 == 1 and char10 == 0 and kernelenc1[i] == kernelenc2[v30val % (kernelenc2[i] * kernelenc2[i] * kernelenc2[i] + kernelenc2[i] * kernelenc2[i] + 27) % 512]):
			char10 += 1
			o += target[i]
			break

print(o + "}")