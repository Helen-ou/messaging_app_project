import socket
import threading
import tkinter as tk
from time import sleep
from random import randint
from caesar_cipher import caesar_ciphering, caesar_deciphering

nickname = input("Choisissez un pseudo: ")
KEY_CAESAR = randint(1, 25)

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive(callback=None):
    compteur_key = 0
    while True:
        try:
            message = client.recv(1024)
            if message:
                if not compteur_key:
                    decoded_key = int(message.decode('utf-8'))
                    compteur_key += 1
                elif callback:
                    callback(caesar_deciphering(message.decode('utf-8'), decoded_key))
                    compteur_key = 0
                else:
                    print(caesar_deciphering(message.decode('utf-8'), decoded_key))
                    compteur_key = 0
            else:
                break
        except Exception as e:
            print(f"Erreur lors de la réception: {e}")
            client.close()
            break

def write(message=None):
    if message:
        full_message = f"{nickname}: {message}"
        client.send(str(KEY_CAESAR).encode('utf-8'))
        sleep(0.1)
        client.send((caesar_ciphering(full_message, KEY_CAESAR)).encode('utf-8'))
    else:
        while True:
            message = input('')
            full_message = f"{nickname}: {message}"
            client.send(str(KEY_CAESAR).encode('utf-8'))
            sleep(0.1)
            client.send((caesar_ciphering(full_message, KEY_CAESAR)).encode('utf-8'))

if __name__ == "__main__":
    from gui import ChatClient
    root = tk.Tk()
    chat_client = ChatClient(root, receive, write, nickname)
    root.mainloop()

