import socket
import threading
import json
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import bcrypt

HOST = '127.0.0.1'
PORT = 12345
USER_FILE = "users.json"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}  # {username: (client_socket, public_key)}

server_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
server_public_key = server_private_key.public_key()
server_public_pem = server_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = hashed_password
    save_users(users)
    return True

def authenticate_user(username, password):
    users = load_users()
    return username in users and bcrypt.checkpw(password.encode(), users[username].encode())

def broadcast(message, sender_username):
    """ Chiffre et envoie le message à tous les autres clients. """
    for username, (client, public_key) in clients.items():
        if username != sender_username:
            try:
                encrypted_message = public_key.encrypt(
                    message.encode(),
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                client.send(encrypted_message)
            except Exception as e:
                print(f"Erreur d'envoi à {username} : {e}")
                remove_client(username)

def handle_client(client):
    try:
        client.send(server_public_pem)  # Envoi de la clé publique du serveur
        client.send(b"LOGIN_OR_REGISTER")

        data = client.recv(1024).decode()
        action, username, password = data.split('|')

        if action == "REGISTER":
            success = register_user(username, password)
            client.send(b"REGISTER_SUCCESS" if success else b"REGISTER_FAIL")
        elif action == "LOGIN":
            if authenticate_user(username, password):
                client.send(b"LOGIN_SUCCESS")
            else:
                client.send(b"LOGIN_FAIL")
                client.close()
                return

        # Récupérer la clé publique du client
        client_public_pem = client.recv(4096)
        client_public_key = serialization.load_pem_public_key(client_public_pem)

        clients[username] = (client, client_public_key)  # Stocker la connexion et la clé publique

        while True:
            encrypted_message = client.recv(4096)
            if not encrypted_message:
                break

            message = server_private_key.decrypt(
                encrypted_message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            ).decode('utf-8')

            print(f"Message reçu: {message}")
            broadcast(message, username)  # Diffuser aux autres clients

    except Exception as e:
        print(f"Erreur: {e}")
    finally:
        remove_client(username)

def remove_client(username):
    if username in clients:
        clients[username][0].close()
        del clients[username]

def receive_connections():
    print(f"Le serveur écoute sur {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        print(f"Connexion de {address}")
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == "__main__":
    receive_connections()
