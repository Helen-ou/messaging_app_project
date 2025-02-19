Le chiffrement RSA présenté-ci dessous est un algorithme de cryptographie asymétrique reposant sur un couple de clés : une clé publique pour chiffrer les messages et une clé privée pour les déchiffrer.

Lorsqu’un utilisateur envoie un message, celui-ci est chiffré avec la clé publique du destinataire, garantissant que seul le possesseur de la clé privée peut le déchiffrer. 

Dans notre application, chaque client génère sa propre paire de clés RSA. Lors de la connexion, la clé publique est échangée avec le serveur, permettant de chiffrer les messages avant leur envoi. Une fois reçus, ces messages doivent être déchiffrés par la clé privée correspondante.

Nous avons vérifié le fonctionnement de ce système en envoyant la clé privé sur l'onglet serveur et en demandant l'envoi du message chiffré avant déchiffrement. Nous l'avons ensuite déchiffré à l'aide de Cyberchef, ce qui a donné le screenshot :

RSA : ![](AES_CyberChef.png) 

Dans ce contexte, RSA assure un haut niveau de sécurité, tant que les clés privées restent secrètes et ne sont pas compromises.
