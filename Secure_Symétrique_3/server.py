import socket
import threading

# Adresse et port du serveur
HOST = '127.0.0.1'
PORT = 12345

# Création du socket serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []  # liste des clients connectés

def broadcast(message, client_sender):
    """
    Envoie un message à tous les clients sauf l'émetteur.
    """
    for client in clients:
        if client != client_sender:
            try:
                client.send(message)
            except Exception as e:
                print(f"Erreur lors de l'envoi à un client: {e}")
                clients.remove(client)

def handle_client(client):
    """
    Gère la réception des messages d'un client.
    """
    while True:
        try:
            # Réception d'un message (en clair)
            message = client.recv(1024)
            if message:
                print(f"Message reçu: {message.decode('utf-8')}")
                broadcast(message, client)
            else:
                remove_client(client)
                break
        except Exception as e:
            print(f"Erreur: {e}")
            remove_client(client)
            break

def remove_client(client):
    """
    Retire le client de la liste et ferme sa connexion.
    """
    if client in clients:
        clients.remove(client)
        client.close()

def receive_connections():
    """
    Accepte les connexions entrantes et démarre un thread pour chaque client.
    """
    print(f"Le serveur est en écoute sur {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        print(f"Connexion de {address}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive_connections()
