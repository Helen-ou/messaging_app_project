Un bruteforce d'un message chiffré à cette étape là est très difficile :
Avec une clé de 25 de longueur et un chiffrement caesar, il faudra en moyenne ce montant d'essais pour déchiffrer de force un message :
$26^{26} \times 26 = 26^{27}$

D'autres attaques sont tout de même possibles, par exemple en se fiant sur les lettres les plus communes de l'alphabet, mais cela va nécessiter des messages plus long que court.


Cependant, comme les clés sont stockées localement cette application est très vulnérable à du reverse engineering.
De fait, nous pourrions donc récupérer la fonction "decrypt" (en assembleur) et passer les messages récupérés dans celle-ci.
