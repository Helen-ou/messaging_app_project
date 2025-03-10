from Crypto.Cipher import AES
import base64

key = b'YELLOW SUBMARINE'

file_path = r"C:\Users\Dominique Husson\Downloads\encoded.txt"
with open(file_path, "r") as f:
    encoded_data = f.read()

ciphertext = base64.b64decode(encoded_data)

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

decrypted_text = plaintext.decode('utf-8', errors='ignore')
print(decrypted_text)
