import time 

input_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

start_time = time.time()

def print_xored_input_from_alphabet(input_hex, alphabet):
    xor_array = []
    for letter in alphabet:
        xored_input = ""
        for i in range(0, len(input_hex), 2):
            xored_input += chr(int(input_hex[i:i+2], 16) ^ ord(letter))
        if xored_input.count(" ") > 0:
            xored_input = xor_array.append([xored_input, letter])
    return xor_array

print(print_xored_input_from_alphabet(input_hex, alphabet))

print("--- %s seconds ---" % (time.time() - start_time))
# Cooking MC's like a pound of bacon