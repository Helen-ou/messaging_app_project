import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, client_sender):
    for client in clients:
        if client != client_sender:
            try:
                client.send(message)
            except Exception as e:
                print(f"Erreur lors de l'envoi à un client: {e}")
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(f"Message reçu (chiffré): {message}")
                broadcast(message, client)
            else:
                remove_client(client)
                break
        except Exception as e:
            print(f"Erreur: {e}")
            remove_client(client)
            break

def remove_client(client):
    if client in clients:
        clients.remove(client)
        client.close()

def receive_connections():
    print(f"Le serveur est en écoute sur {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        print(f"Connexion de {address}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_connections()
