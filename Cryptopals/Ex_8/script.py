from Crypto.Cipher import AES
import base64

# Define the key (16 bytes for AES-128)
key = b'YELLOW SUBMARINE'

# Read the Base64-encoded ciphertext from the file
file_path = r"C:\Users\Dominique Husson\Downloads\encoded.txt"
with open(file_path, "r") as f:
    encoded_data = f.read()

# Decode from Base64
ciphertext = base64.b64decode(encoded_data)

# Decrypt using AES-128 in ECB mode
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

# Decode and print the decrypted text
decrypted_text = plaintext.decode('utf-8', errors='ignore')
print(decrypted_text)
