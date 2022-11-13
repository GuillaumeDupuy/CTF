import base64
from Crypto.Cipher import AES
import hashlib

msg = "fD3kitB7aiTuyjuKflZw4O4KX8+t6pHkzr8EGirMByk="
Key = "e26db845ae634c7d774f8924a565e34e215b659a97c7e1d01a401fea7c5f6d87"
IV = "00000000000000000000000000000000"
key_dec = bytes.fromhex(Key)
IV = bytes.fromhex(IV)
encryption = base64.b64decode(msg)
cipher = AES.new(key_dec, AES.MODE_CBC, IV)
decrypt = cipher.decrypt(encryption)
print(decrypt)