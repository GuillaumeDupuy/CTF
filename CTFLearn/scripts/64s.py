import base64
from io import open

count = 0
with open("ctf.txt",encoding='utf-8') as f:
    ctext = f.read()

while True:
  count += 1
  ctext=base64.b64decode(ctext)
  if "ABCTF" in str(ctext):
      print(ctext.decode("utf-8"))
      break
      