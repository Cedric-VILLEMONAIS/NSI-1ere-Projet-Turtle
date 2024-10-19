# Documentation :
<a href="https://docs.python.org/fr/3/library/turtle.html" target="_blank">Documentation officielle</a>

<a href="https://github.com/Cedric-VILLEMONAIS/Python-Turtle-Documentation" target="_blank">Ma dcumentation</a>

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Un coucher de soleil avec des nuages sur une plage avec la mer et des poissons et sur la plage des chateaux de sables. On peut mettre des oiseaux qui volent dans le ciel.

**Coucher de soleil :** Faire un cercle pour le soleil avec pour le coucher de soleil des petits cercles autours avec un dégradé (pour le dégradé faire une fonction qui trace plein de petits cercles autour du soleil avec une boucle qui active l'autre fonction avec comme un système d'incrémentation sur le code hexadécimal de la couleur. Cette deuxième fonction s'appellera gradient() prendra pour arguments (couleur_départ_hex, couleur_fin_hex)

**Nuages :** Faire une fonction nuage(x_depart, x_fin, y_depart, y_fin, nb_nuages) qui va créer créer un nombre de nuages donné. Pour la taille des nuages faire un random randint()

**Plage :** Faire une plage d'une taille plus ou moins grande. Pour la taille de la plage faire des calculs pour que sa taille s'adapte en fonction de l'horaire choisi par l'utilisateur

**Mer :** voire s'il n'est pas possible de faire un effet pour avoir l'impression que l'eau arrive du fond de l'image si c'est techniquement possible

**Animaux aquatiques :** Essayer de créer plusieurs tortues en même temps avec des variables et avec turtle shape() voir s'il est techniquement possible de mettre un poisson et d'en fonction de la position de la mer sur le dessin faire en sorte qu'il bouge à des postitions aléatoires. Essayer de faire aussi avec des boucles while en changeant l'apparence du turtle afin qu'on ai un effet de poisson qui nage --> register_shape()

**Chateaux de sables :** avec un random randint créer un nombre aléatoire de chateaux avec des tailles aléatoires

**Utiliser éléments du cours :**
- Fonctions avec des valeurs par défaut
- La fonction lambda
- Penser aux variables globales et locales
- **Documenter les fonctions et le code (cours 3.)**
- **Effectuer des tests avec le module doctest et les conditions try et expect (cours 3.)**

**Demander à l'utilisateur :** (utiliser numinput() : ex : numinput("Heure", "Quelle heure entre 18 et 22 ?", minval=18, maxval=22)
-  Quelle heure entre par ex (18 et 22) et adapter en fonction la couleur d'arrière plan ainsi que la couleur du soleil
- Si le temps est nuageux ou pas et adapter ainsi le nombre de nuages
- Si c'est des petits ou gros nuages et ainsi adapter le random randint()
