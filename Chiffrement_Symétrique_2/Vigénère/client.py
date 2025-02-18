import socket
import threading
from vigenere_cipher import vigenere_cipher  # Import the encryption function
import unicodedata
# Clé unique pour chiffrer et déchiffrer
SECRET_KEY = "HIHIHAHA"

# Saisie du pseudo de l'utilisateur
nickname = input("Choisissez un pseudo: ")

# Adresse et port du serveur
HOST = '127.0.0.1'
PORT = 12345

# Création du socket client et connexion au serveur
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def normalize_text(text):
    """ Normalise les caractères en supprimant les accents. """
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

def receive():
    """
    Réception et déchiffrement des messages envoyés par le serveur.
    """
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                # Séparer pseudo et message chiffré
                if ":" in message:
                    encrypted_nickname, encrypted_message = message.split(":", 1)
                    decrypted_nickname = vigenere_cipher(encrypted_nickname.strip(), SECRET_KEY, encrypt=False)
                    decrypted_message = vigenere_cipher(encrypted_message.strip(), SECRET_KEY, encrypt=False)
                    print(f"{decrypted_nickname}: {decrypted_message}")
                else:
                    print(message)
            else:
                break
        except Exception as e:
            print(f"Erreur lors de la réception: {e}")
            client.close()
            break

def write():
    """
    Chiffre et envoie les messages saisis par l'utilisateur au serveur.
    """
    while True:
        message = input('')
        encrypted_nickname = vigenere_cipher(nickname, SECRET_KEY) 
        encrypted_message = vigenere_cipher(message, SECRET_KEY)    
        full_message = f"{encrypted_nickname}: {encrypted_message}"
        client.send(full_message.encode('utf-8'))

# Démarrage des threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()