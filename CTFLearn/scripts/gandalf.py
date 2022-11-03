import base64

string1 = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
string2 = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

a = string1
A = base64.b64decode(a)

b = string2
B = base64.b64decode(b)

c = []
l = len(A)

i = 0
while i < l:
  c.append(chr(A[i] ^ B[i]))
  i += 1

print(''.join(c))