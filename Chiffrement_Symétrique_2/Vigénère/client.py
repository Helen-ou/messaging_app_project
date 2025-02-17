import socket
import threading

# Fonction de chiffrement et déchiffrement Vigenère
def vigenere_cipher(text, key, encrypt=True):
    key = key.upper()
    result = []
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha():  # Vérifie si c'est une lettre
            shift = ord(key[key_index % key_length]) - ord('A')
            if not encrypt:
                shift = -shift
            
            # Gestion majuscules et minuscules indépendamment
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr(((ord(char) - base + shift) % 26) + base)
            
            result.append(new_char)
            key_index += 1  # La clé avance seulement sur les lettres
        else:
            result.append(char)  # Les caractères spéciaux ne changent pas

    return ''.join(result)

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
        encrypted_nickname = vigenere_cipher(nickname, SECRET_KEY)  # Chiffre le pseudo
        encrypted_message = vigenere_cipher(message, SECRET_KEY)    # Chiffre le message
        full_message = f"{encrypted_nickname}: {encrypted_message}"
        client.send(full_message.encode('utf-8'))

# Démarrage des threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
