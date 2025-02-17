import unicodedata

def normalize_text(text):
    """ Normalise les caractères en supprimant les accents. """
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if unicodedata.category(c) != 'Mn')

def vigenere_cipher(text, key, encrypt=True):
    key = normalize_text(key).upper()  # Supprime les accents de la clé
    result = []
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha():
            normalized_char = normalize_text(char)  # Supprime les accents du caractère
            shift = ord(key[key_index % key_length]) - ord('A')
            if not encrypt:
                shift = -shift

            base = ord('A') if normalized_char.isupper() else ord('a')
            new_char = chr(((ord(normalized_char) - base + shift) % 26) + base)

            # Rétablir la casse d'origine
            if char.islower():
                new_char = new_char.lower()

            result.append(new_char)
            key_index += 1
        else:
            result.append(char)  # Garde les caractères spéciaux inchangés

    return ''.join(result)


"""test = "Hello, World!"
encrypted_text = vigenere_cipher(test, SECRET_KEY, encrypt=True)
decrypted_text = vigenere_cipher(encrypted_text, SECRET_KEY, encrypt=False)
print(f"Texte clair: {test}")
print(f"Texte chiffré: {encrypted_text}")
print(f"Texte déchiffré: {decrypted_text}")"""