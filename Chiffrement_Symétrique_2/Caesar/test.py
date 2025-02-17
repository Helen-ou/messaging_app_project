x ="21\nowo"
print(int(x[:2]))

import caesar_cipher

KEY = 5

x = str(KEY) + " " + caesar_cipher.caesar_ciphering("owo", KEY)
print(x)
y = int(x[:2])
print(y)