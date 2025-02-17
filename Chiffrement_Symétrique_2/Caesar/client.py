import socket
import threading
from time import sleep
from random import randint
from caesar_cipher import caesar_ciphering, caesar_deciphering

# Saisie du pseudo de l'utilisateur
nickname = input("Choisissez un pseudo: ")
KEY_CAESAR = randint(1, 25)

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
    compteur_key = 0
    while True:
        try:
            message = client.recv(1024)
            if message:
                if not compteur_key:
                    decoded_key = int(message.decode('utf-8'))
                    compteur_key += 1
                else:
                    print(caesar_deciphering(message.decode('utf-8'), decoded_key))
                    compteur_key = 0
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
        client.send(str(KEY_CAESAR).encode('utf-8'))
        sleep(0.1)
        client.send((caesar_ciphering(full_message, KEY_CAESAR)).encode('utf-8'))

# Démarrage des threads pour la réception et l'envoi des messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


