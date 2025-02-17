def caesar_cyphering(text):
    shift = 8 # Clé de chiffrement 
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decyphering(text):
    shift = 8 # Clé de déchiffrement
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result


"""test = "Hello, World!"
print(f"Texte clair: {test}")
print(f"Texte chiffré: {caesar_cyphering(test)}")
print(f"Texte déchiffré: {caesar_decyphering(caesar_cyphering(test))}")"""