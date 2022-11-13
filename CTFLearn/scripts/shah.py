import base64
from Crypto.Cipher import AES
import hashlib

msg = "TZm1GWpQfUB+7cM2BIng5MCeEgBqxIKunpThaVKemNBmvbis9H0rTAOSIYXsu8va.CK6Z67gNHOQYBPUNl1mY6jWVLfq+5FmUtaW/lnYT71rBlmPcBLymDGFj2BJjZWY4.A3aM2Mp0AGDPrK3X4eMu8Q=="
Key = "b18ef1351fc0df641abbe56dcd4928a8bb98452b1b43d8c1c13f1874c8b35056"
IV = "00000000000000000000000000000000"

key_dec = bytes.fromhex(Key)
IV = bytes.fromhex(IV)
encryption = base64.b64decode(msg)
cipher = AES.new(key_dec, AES.MODE_CBC, IV)
decrypt = cipher.decrypt(encryption)
print(decrypt)