import socket
import threading
import tkinter as tk
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

SECRET_KEY = b"Cle1234567890123"

nickname = input("Choisissez un pseudo: ")

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def encrypt_message(message, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
    return iv + encrypted_message  

def decrypt_message(encrypted_message, key):
    iv = encrypted_message[:16]
    cipher_message = encrypted_message[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(cipher_message) + decryptor.finalize()
    return decrypted_message.decode(errors='ignore')

def receive(callback=None):
    while True:
        try:
            encrypted_message = client.recv(1024)
            if encrypted_message:
                decrypted_message = decrypt_message(encrypted_message, SECRET_KEY)
                if callback:
                    callback(decrypted_message)
                else:
                    print(decrypted_message)
            else:
                break
        except Exception as e:
            print(f"Erreur lors de la réception: {e}")
            client.close()
            break

def write(message):
    encrypted_message = encrypt_message(f"{nickname}: {message}", SECRET_KEY)
    client.send(encrypted_message)

if __name__ == "__main__":
    from gui import ChatClient
    root = tk.Tk()
    chat_client = ChatClient(root, receive, write, nickname)
    root.mainloop()