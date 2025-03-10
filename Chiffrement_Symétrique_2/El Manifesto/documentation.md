Pour décoder le message, nous avons d'abord déterminé la longueur de sa clé. En utilisant une plateforme en ligne, nous avons pu identifier les deux premières lettres, ce qui nous a permis de progresser plus rapidement en devinant le premier mot, "Ce".  

Nous avons ensuite modifié un script trouvé sur GitHub (size_key.py), conçu pour compléter une clé partiellement connue en s'appuyant sur le texte déjà déchiffré. Grâce à cet outil, nous avons identifié "GuardiaLyon" comme clé probable. En affinant notre recherche à l'aide d'une autre plateforme de déchiffrement, nous avons confirmé que la clé complète était **"GuardiaLyonGuardia"**.  

Enfin, en utilisant un script Python nommé decode_vigenere.py, nous avons réussi à déchiffrer l'intégralité du message. 