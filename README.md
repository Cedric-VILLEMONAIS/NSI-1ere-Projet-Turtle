# 1ère NSI - 2024-2025 - Projet Python avec le module Turtle - Nora TERRAL et Cédric VILLEMONAIS
## Documentation :
<a href="https://docs.python.org/fr/3/library/turtle.html" target="_blank">Documentation officielle</a>

<a href="https://github.com/Cedric-VILLEMONAIS/Python-Turtle-Documentation" target="_blank">Ma dcumentation</a>

## Description du projet :
### Analyse du travail :
Dans notre projet nous avons réalisé un coucher de soleil. Nous demandons à l'utilisateur l'heure qu'il souhaite ainsi que s'il souhaite des nuages. En fonction de l'heure donné par l'utilisateur les couleurs s'adaptent. Notre projet dessine le soleil, la mer, la plage le reflet du soleil dans l'eau, des poissons, des vagues, de l'écume, un palmier, des nuages, des étoiles fonction de l'heure et des oiseaux qui sont animés et volent.

### Amélioration possibles :
Si nous avions eu plus de temps nos améliorations possibles sont la création d'un dégradé autour du soleil ainsi que faire des châteaux de sable sur la plage

## Répartition des tâches réalisées :
### Cédric :
- Création du repository GitHub
- Création du fichier modules.py pour pouvoir unifier tous les modules et variables dans un seul fichier à importer :
    - Création de la fonction init :
        - Création de la fenêtre d'affichage (Résolution, title et positionnement sur l'écran de l'utilisateur)
        - Affichage d'un message d'avertissement consernant la résolution minimale et la fonction teleport du module ```turtle()``` qui ne fonctionne pas sur thonny
        - Création des variables qui recueillent les choix de l'utililateur
        - Changement de la couleur de l'arrière plan en fonction de l'heure choisi par l'utilisateur
        - Initialisation de l'orientation par défaut ainsi que la vitesse par défaut
    - Globalisation des variables des choix de l'utililateur pour une utilisation à travers tous les fichiers du projet
    - Importation des modules nécessaires au projet
- Configuration du projet pour un fonctionnement en plusieurs fichiers
- Création du fichier main.py et importation des différents modules et fichiers
- Création de la fonction ```cloud()``` qui dessine des nuages à des positions et tailles aléatoires
- Création de la fonction ```beach()``` qui dessine la plage aux coordonnées données
- Création de la fonction ```bird()``` qui est une annimation qui fait voler des oiseax
- Création de la fonction ```bird()``` qui est une annimation qui fait voler des oiseax
- Documentation des fichiers cloud.py, init.py, beach.py et bird.py
- Documentation de toutes les fonctions du code avec """ """


### Nora :
- idée du dessin pour le projet
- Création de la fonction: ```sunset()``` qui dessine un soleil différent en fonction de l'heure choisie par l'utilisateur pour simuler un coucher de soleil  
- Création de la fonction: ```sea()``` qui dessine la mer aux coordonnées données suivant l'heure choisie par l'utilisateur
- Création de la fonction: ```fish()``` qui dessine des poissons à des positions, orientations aléatoires ainsi que la taille étant légèrement aléatoire pour créer un effet de profondeur
- Création de la fonction: ```waves()``` qui dessine des vagues à des positions aléatoires et avec une épaisseur aléatoire
- Création de la fonction: ```palmtree()``` qui dessine un palmier avec des couleurs différentes en fonction de l'heure choisie par l'utilisateur
- Création de la fonction: ```ecume()``` qui dessine une écume aux coordonnées données et à des proportions aléatoires pour faire un effet mouvementé
- Création de la fonction: ```reflection()``` qui dessine la réflection du soleil sur la mer suivant l'heure 
- A essayé de créer une fonction ```gradient()``` pour faire des dégradés
- création des fichiers sunset.py, sea.py, fish.py, waves.py, palmtree.py, ecume.py, reflection.py, gradient.py
- Documentation des fichiers sunset.py, sea.py, fish.py, waves.py, palmtree.py, ecume.py, reflection.py, gradient.py 
- Documentation du fichier main pour l'exécution des fonctions



