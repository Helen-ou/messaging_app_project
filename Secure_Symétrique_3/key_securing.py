from cryptography.fernet import Fernet
def encrypt(inputed):
    key_str = "qwertyuiopasdfghjklzxcvbnm"
    key_int = "S3cr3t-K3y"
    if type(inputed) == str:
        substitution_map = {}
        for i in range(26):
            substitution_map[chr(97 + i)] = key_str[i]
        encrypted_text = ""

        for char in inputed:
            if char.islower():
                encrypted_text += substitution_map[char]
            else:
                encrypted_text += char
        return encrypted_text
    elif type(inputed) == int:
        inputed *= 0x1337
        for i in key_int:
            if ord(i) % 2 == 0:
                inputed += ord(i) * 4
            else:
                inputed -= ord(i) * 7
        return (inputed)
    
def decrypt(inputed):
    key_str = "qwertyuiopasdfghjklzxcvbnm"
    key_int = "S3cr3t-K3y"
    if type(inputed) == str:
        substitution_map = {}
        for i in range(26):
            substitution_map[key_str[i]] = chr(97 + i)
        decrypted_text = ""

        for char in inputed:
            if char.islower():
                decrypted_text += substitution_map[char]
            else:
                decrypted_text += char
        return decrypted_text
    elif type(inputed) == int:
        for i in key_int:
            if ord(i) % 2 == 0:
                inputed -= ord(i) * 4
            else:
                inputed += ord(i) * 7
        return (inputed // 0x1337)
    
