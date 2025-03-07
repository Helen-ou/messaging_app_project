import time
import os
import base64

start_time = time.time()

with open(os.path.join(os.path.dirname(__file__), 'dat_6.txt')) as r:
    array_input_b64 = r.read().splitlines()

input_b64 = ""
for x in array_input_b64:
    input_b64 += x
input_xor = base64.b64decode(input_b64)

def hamming_distance(ref_text, text):
    distance = 0
    for i in range(len(ref_text)):
        distance += bin(ord(ref_text[i]) ^ ord(text[i])).count('1')
    return distance

def find_keysize(text_input):
    keysize = 0
    min_distance = 1000
    for i in range(2, 40):
        distance = 0
        for j in range(0, len(text_input), i):
            distance += hamming_distance(text_input[j:j+i], text_input[j+i:j+2*i])
        distance /= i
        distance /= len(text_input) / i
        if distance < min_distance:
            min_distance = distance
            keysize = i
    return keysize

def decrypt(b64_input, keysize):
    pass

print(hamming_distance("this is a test", "wokka wokka!!!"))
print(find_keysize(input_b64))
print(decrypt(input_b64, find_keysize(input_b64)))
print("--- %s seconds ---" % (time.time() - start_time))