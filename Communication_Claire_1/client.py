import socket
import threading
import tkinter as tk

nickname = input("Choisissez un pseudo: ")

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive(callback=None):
    while True:
        try:
            message = client.recv(1024)
            if message:
                decoded_message = message.decode('utf-8')
                if callback:
                    callback(decoded_message)
                else:
                    print(decoded_message)
            else:
                break
        except Exception as e:
            print(f"Erreur lors de la réception: {e}")
            client.close()
            break

def write(message=None):
    if message:
        full_message = f"{nickname}: {message}"
        client.send(full_message.encode('utf-8'))
    else:
        while True:
            message = input('')
            full_message = f"{nickname}: {message}"
            client.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    from gui import ChatClient
    root = tk.Tk()
    chat_client = ChatClient(root, receive, write, nickname)
    root.mainloop()
