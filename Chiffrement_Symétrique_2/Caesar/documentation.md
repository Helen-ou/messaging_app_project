Le message encodé en hexadécimal à été récupéré dans Wireshark encore une fois, puis brute force dans Cyberchef. A noter que les algorithmes de déchiffrement seront fait plus tard dans la chronologie du projet, et que Cyberchef est la solution en attendant.
On le retrouve au cran 18, ou 26-8.


Ce qui semble être la clé au vu de sa taille : 
![alt text](cle_encode.png)

Puis le texte : 
![alt text](texte_encode.png)

On décode sur Cyberchef avec une rotation de -16, l'opposé de 16 : 

![alt text](cyberchef.png)