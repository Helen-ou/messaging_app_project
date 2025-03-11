import os 
import time

start_time = time.time()

with open(os.path.join(os.path.dirname(__file__), 'Cryptopals/Set_1/dat_4.txt')) as r:
    input_hex = r.read().splitlines()
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"


def print_xored_input_from_alphabet(input_hex, alphabet):
    xor_array = []
    for letter in alphabet:
        for i in range(len(input_hex)):
            xored_input = ""
            for j in range(0, len(input_hex[i]), 2):
                xored_input += chr(int(input_hex[i][j:j+2], 16) ^ ord(letter))
            if xored_input.count(" ") > 3:
                xored_input = xor_array.append((xored_input, i))
    return xor_array

print((print_xored_input_from_alphabet(input_hex, alphabet)))

print("--- %s seconds ---" % (time.time() - start_time))