import socket
import threading
import tkinter as tk
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

def receive(callback=None):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                if ":" in message:
                    encrypted_nickname, encrypted_message = message.split(":", 1)
                    decrypted_nickname = vigenere_cipher(encrypted_nickname.strip(), SECRET_KEY, encrypt=False)
                    decrypted_message = vigenere_cipher(encrypted_message.strip(), SECRET_KEY, encrypt=False)
                    if callback:
                        callback(f"{decrypted_nickname}: {decrypted_message}")
                    else:
                        print(f"{decrypted_nickname}: {decrypted_message}")
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
        encrypted_nickname = vigenere_cipher(nickname, SECRET_KEY) 
        encrypted_message = vigenere_cipher(message, SECRET_KEY)    
        full_message = f"{encrypted_nickname}: {encrypted_message}"
        client.send(full_message.encode('utf-8'))
    else:
        while True:
            message = input('')
            encrypted_nickname = vigenere_cipher(nickname, SECRET_KEY) 
            encrypted_message = vigenere_cipher(message, SECRET_KEY)    
            full_message = f"{encrypted_nickname}: {encrypted_message}"
            client.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    from gui import ChatClient
    root = tk.Tk()
    chat_client = ChatClient(root, receive, write, nickname)
    root.mainloop()