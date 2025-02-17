import socket
import threading

# Saisie du pseudo de l'utilisateur
nickname = input("Choisissez un pseudo: ")

# Adresse et port du serveur (doivent correspondre à ceux du serveur)
HOST = '127.0.0.1'
PORT = 12345

# Création du socket client et connexion au serveur
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    """
    Réception des messages envoyés par le serveur.
    """
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(message.decode('utf-8'))
            else:
                # La connexion a été fermée
                break
        except Exception as e:
            print(f"Erreur lors de la réception: {e}")
            client.close()
            break

def write():
    """
    Envoie les messages saisis par l'utilisateur au serveur.
    """
    while True:
        message = input('')
        full_message = f"{nickname}: {message}"
        client.send(full_message.encode('utf-8'))

# Démarrage des threads pour la réception et l'envoi des messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
