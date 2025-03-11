from Crypto.Cipher import AES
import base64
import os 

key = b'YELLOW SUBMARINE'

with open(os.path.join(os.path.dirname(__file__), 'encoded.txt')) as r:
    encoded_data = r.read()

ciphertext = base64.b64decode(encoded_data)

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

decrypted_text = plaintext.decode('utf-8', errors='ignore')
print(decrypted_text)
