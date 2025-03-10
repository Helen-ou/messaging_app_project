import time

input_text = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

start_time = time.time()

def repeating_key_XOR(text, key):
    output = "" 
    for i in range(len(text)):
        output += format(ord(text[i]) ^ ord(key[i % len(key)]), '02x')
    return output

print(repeating_key_XOR(input_text, key))

print("--- %s seconds ---" % (time.time() - start_time))