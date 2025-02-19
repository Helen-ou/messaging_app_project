input_hex = "0x1c0111001f010100061a024b53535009181c"
input_key = "0x686974207468652062756c6c277320657965"

# print(bin(int(input_hex, 16)).zfill(8))
# print(bin(int(input_key, 16)).zfill(8))
x = hex(int(input_hex, 16) ^ int(input_key, 16))[2:]
print(x)