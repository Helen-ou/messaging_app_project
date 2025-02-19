Pour effectuer une attaque Man-in-the-Middle sur notre application, nous devons nous possitionner en tant qu'attaquant. 

Sachant que notre application ne passe pas par la carte réseau et reste en localhost:12345, nous pouvons utiliser Wireshark, en le plaçant en mode loopback (mode permettant d'analyser les flux ne passant pas par la carte réseau) avec le filtre suivant : tcp.port == 12345

Nous nous sommes placés comme attaquant dans toutes les différentes possibilitées que nous avons crées, et nous avons pris des screenshots de ce qui a pu être récupéré.

Une fois les documents récupéré, un utilisateur malveillant peut se servir de Cyberchef afin de déchiffrer le message (copies d'écran à l'appui) :

CAESAR (non sécurisé) : ![](Caesar_Wireshark.png) ![](Caesar_CyberChef.png)
VIGENERE (non sécurisé) :  ![](Vigenere_Wireshark.png) ![](Vigenere_CyberChef.png)
AES : ![](AES_Wireshark.png) 
RSA : ![](RSA_Wireshark.png) 

Dépendant de la force du chiffrement et de la sécurisation, il se peut que l'attaquant récupère quelque chose qui ne puisse pas être déchiffré, notamment dans le cas d'un hash ou d'un chiffrement à clé asymétrique. 