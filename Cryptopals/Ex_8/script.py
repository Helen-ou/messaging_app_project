from collections import Counter

# Détecte les blocs de 16 bytes répétés dans un cyphertexte
def detect_ecb(ciphertexts):
    ecb_candidates = []
    for i, hex_ct in enumerate(ciphertexts):
        raw_ct = bytes.fromhex(hex_ct)  # Convertit le hex en bytes
        blocks = [raw_ct[j:j+16] for j in range(0, len(raw_ct), 16)]  # sépare en des blocs de 16 bytes
        num_repeats = len(blocks) - len(set(blocks))  
        if num_repeats > 0:  # Plus ça se répète plus il y a de chances que ce soit du ECB
            ecb_candidates.append((i, num_repeats, hex_ct))
    
    # Trie par celui qui a le plus de répétitions
    ecb_candidates.sort(key=lambda x: x[1], reverse=True)
    return ecb_candidates

file_path = r"C:\Users\Dominique Husson\Documents\GitHub\messaging_app_project\Cryptopals\Ex_8\encoded_cyphertext.txt"
with open(file_path, "r") as f:
    hex_ciphertexts = f.read().splitlines()

# Détecte le cyphertexte crypté en ECD
ecb_detected = detect_ecb(hex_ciphertexts)

# Affiche la ligne ECD
if ecb_detected:
    line_number, repeats, ciphertext = ecb_detected[0]
    print(f"A la ligne {line_number + 1} avec {repeats} répétition, il se peut que ça soit de l'ECB :")
    print(ciphertext)
else:
    print("Pas d'ECB détecté")
