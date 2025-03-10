import socket
import threading
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

server_public_pem = client.recv(4096)
server_public_key = serialization.load_pem_public_key(server_public_pem)

server_message = client.recv(1024).decode()
print(f"Message du serveur: {server_message}")

nickname = input("Choisissez un pseudo: ")
password = input("Choisissez un mot de passe: ")
action = input("Voulez-vous vous inscrire (REGISTER) ou vous connecter (LOGIN) ? ").upper()

client.send(f"{action}|{nickname}|{password}".encode())
response = client.recv(1024).decode()

if response in ["LOGIN_FAIL", "REGISTER_FAIL"]:
    print("Échec de l'authentification. Fermeture de la connexion.")
    client.close()
    exit()
else:
    print("Connexion réussie !")

client_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
client_public_key = client_private_key.public_key()
client_public_pem = client_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

client.send(client_public_pem)

def receive():
    while True:
        try:
            encrypted_message = client.recv(4096)
            if encrypted_message:
                message = client_private_key.decrypt(
                    encrypted_message,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                ).decode('utf-8')
                print(message)
                print(f"Message chiffré reçu (base64) : {encrypted_message.hex()}")
            else:
                break
        except Exception as e:
            print(f"Erreur de réception: {e}")
            client.close()
            break

def send_message():
    while True:
        message = input()
        encrypted_message = server_public_key.encrypt(
            f"{nickname}: {message}".encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        client.send(encrypted_message)

if __name__ == "__main__":
    receive_thread = threading.Thread(target=receive, daemon=True)
    receive_thread.start()
    
    send_message()
