import itertools

def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    decrypted_text = []
    key_indices = [alphabet.index(k) for k in key]
    key_cycle = itertools.cycle(key_indices)
    
    for char in ciphertext:
        if char in alphabet:
            shift = next(key_cycle)
            index = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text.append(alphabet[index])
        else:
            decrypted_text.append(char)
    
    return "".join(decrypted_text)

ciphertext = """Iy qll autr o rzy etuqt vyu uh bexng nvlej pwn glrvvbaegca..."""
key = "GuardiaLyonGuardia"

decrypted_text = vigenere_decrypt(ciphertext, key)
print(decrypted_text)
