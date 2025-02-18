import socket
import threading
import tkinter as tk
from vigenere_cipher import vigenere_cipher
from caesar_cipher import caesar_ciphering, caesar_deciphering
import unicodedata
from random import randint
from key_securing import encrypt, decrypt

SECRET_KEY_VIGENERE = ""
for i in range(10):
    SECRET_KEY_VIGENERE += chr(randint(65, 90))
print(SECRET_KEY_VIGENERE)
SECRET_KEY_CAESAR = randint(1, 25)

nickname = input("Choisissez un pseudo: ")

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def normalize_text(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

def receive(callback=None):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                if ":" in message:
                    encrypted_nickname, encrypted_message, received_key_vig, received_key_caesar = message.split(":", 3)
                    received_key_vig = decrypt(received_key_vig)
                    received_key_caesar = decrypt(int(received_key_caesar))
                    caesar_decrypted_nickname = caesar_deciphering(encrypted_nickname.strip(), (received_key_caesar))
                    decrypted_nickname = vigenere_cipher(caesar_decrypted_nickname, received_key_vig, encrypt=False)
                    caesar_decrypted_message = caesar_deciphering(encrypted_message.strip(), received_key_caesar)
                    decrypted_message = vigenere_cipher(caesar_decrypted_message, received_key_vig, encrypt=False)
                    if callback:
                        callback(f"{decrypted_nickname} : {decrypted_message}")
                    else:
                        print(f"{decrypted_nickname} : {decrypted_message}")
                else:
                    print(message)
            else:
                break
        except Exception as e:
            print(f"Erreur lors de la réception: {e}")
            client.close()
            break

def write(message=None):
    if message:
        encrypted_nickname = caesar_ciphering(vigenere_cipher(nickname, SECRET_KEY_VIGENERE), SECRET_KEY_CAESAR)
        encrypted_message = caesar_ciphering(vigenere_cipher(message, SECRET_KEY_VIGENERE), SECRET_KEY_CAESAR)
        full_message = f"{encrypted_nickname}:{encrypted_message}:{encrypt(SECRET_KEY_VIGENERE)}:{encrypt(SECRET_KEY_CAESAR)}"
        client.send(full_message.encode('utf-8'))
    else:
        while True:
            message = input('')
            encrypted_nickname = caesar_ciphering(vigenere_cipher(nickname, SECRET_KEY_VIGENERE), SECRET_KEY_CAESAR)
            encrypted_message = caesar_ciphering(vigenere_cipher(message, SECRET_KEY_VIGENERE), SECRET_KEY_CAESAR)
            full_message = f"{encrypted_nickname}:{encrypted_message}:{encrypt(SECRET_KEY_VIGENERE)}:{encrypt(SECRET_KEY_CAESAR)}"
            client.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    from gui import ChatClient
    root = tk.Tk()
    chat_client = ChatClient(root, receive, write, nickname)
    root.mainloop()