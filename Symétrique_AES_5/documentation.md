Ce document décrit l'implémentation du chiffrement AES utilisée dans l'application de chat basée sur des sockets. L'objectif est d'assurer la confidentialité des messages échangés entre les clients en les chiffrant avant envoi et en les déchiffrant à la réception.

L'algorithme de chiffrement utilisé est AES (Advanced Encryption Standard) en mode CFB (Cipher Feedback) avec une clé secrète de 32 octets. 

Chaque message est chiffré avant d'être envoyé au serveur. Le chiffrement se déroule de la manièere suivante :

Un IV (Vecteur d'Initialisation) de 16 octets est généré de manière aléatoire. Puis, le cipher AES est créé en mode CFB avec la clé secrète et l'IV. Le message est ensuite chiffré et retourné en concaténant l'IV et le message chiffré. Chaque message est ensuite déchiffré par la machine en face.

En se placant du PDV de l'attaquant, on remarque avec Wireshark qu'il est possible de récupérer des données mais qu'elles sont tout simplement inutilisable et indéchiffrable facilement.

AES Wireshark : ![](AES_Wireshark.png) 
AES CyberChef : ![](AES_CyberChef.png) 