input_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def print_xored_input_from_alphabet(input_hex, alphabet):
    for letter in alphabet:
        xored_input = ""
        for i in range(0, len(input_hex), 2):
            xored_input += chr(int(input_hex[i:i+2], 16) ^ ord(letter))
        print(xored_input)

print_xored_input_from_alphabet(input_hex, alphabet)

# cOOKINGmcSLIKEAPOUNDOFBACON