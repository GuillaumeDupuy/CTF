from zipfile import ZipFile
import string
import itertools

numbers = string.digits
code = itertools.product(numbers,repeat=5)
zip_file = '1926.zip'
with ZipFile(zip_file) as zf:
    for i in code:
        code = ''.join(i)
        password = "ctflag"+code
        try:
            zf.extractall(pwd=bytes(password,'utf-8'))
            print("[+] password is "+password)
        except:
            pass