import socket
import threading
from vigenere_cipher import vigenere_cipher
import unicodedata

SECRET_KEY = "HIHIHAHA"

nickname = input("Choisissez un pseudo: ")

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def normalize_text(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                if ":" in message:
                    encrypted_nickname, encrypted_message, received_key = message.split(":", 2)
                    decrypted_nickname = vigenere_cipher(encrypted_nickname.strip(), received_key.strip(), encrypt=False)
                    decrypted_message = vigenere_cipher(encrypted_message.strip(), received_key.strip(), encrypt=False)
                    print(f"{decrypted_nickname} (Key: {received_key}): {decrypted_message}")
                else:
                    print(message)
            else:
                break
        except Exception as e:
            print(f"Erreur lors de la réception: {e}")
            client.close()
            break

def write():
    while True:
        message = input('')
        encrypted_nickname = vigenere_cipher(nickname, SECRET_KEY)
        encrypted_message = vigenere_cipher(message, SECRET_KEY)
        full_message = f"{encrypted_nickname}:{encrypted_message}:{SECRET_KEY}"
        print(full_message)
        client.send(full_message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()