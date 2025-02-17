import socket
import threading
from vigenere_cipher import vigenere_cipher
from caesar_cipher import caesar_ciphering, caesar_deciphering
import unicodedata

SECRET_KEY_VIGENERE = "HIHIHAHA"
SECRET_KEY_CAESAR = 8

nickname = input("Choisissez un pseudo: ")

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def normalize_text(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                if ":" in message:
                    encrypted_nickname, encrypted_message, received_key_vig, received_key_caesar = message.split(":", 3)
                    caesar_decrypted_nickname = caesar_deciphering(encrypted_nickname.strip(), int(received_key_caesar.strip()))
                    decrypted_nickname = vigenere_cipher(caesar_decrypted_nickname, received_key_vig.strip(), encrypt=False)
                    caesar_decrypted_message = caesar_deciphering(encrypted_message.strip(), int(received_key_caesar.strip()))
                    decrypted_message = vigenere_cipher(caesar_decrypted_message, received_key_vig.strip(), encrypt=False)
                    print(f"{decrypted_nickname} : {decrypted_message}")
                else:
                    print(message)
            else:
                break
        except Exception as e:
            print(f"Erreur lors de la réception: {e}")
            client.close()
            break

def write():
    while True:
        message = input('')
        encrypted_nickname = caesar_ciphering(vigenere_cipher(nickname, SECRET_KEY_VIGENERE), SECRET_KEY_CAESAR)
        encrypted_message = caesar_ciphering(vigenere_cipher(message, SECRET_KEY_VIGENERE), SECRET_KEY_CAESAR)
        full_message = f"{encrypted_nickname}:{encrypted_message}:{SECRET_KEY_VIGENERE}:{SECRET_KEY_CAESAR}"
        client.send(full_message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()