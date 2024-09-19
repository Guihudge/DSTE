# Programmation threads
## Exo 1
### Quel est le rôle du crible d’Erathostène ?
Le crible d’Erathostène est une méthode permétant de calculer les nombre premiers de 2 à N, où N est fixé par l'utilisateur.

### Expliquer son fonctionnement
On commance par crée un table de 2 à N. On raye tout les multiple de 2 jusqu'à arriver à la fin du tableau, on prend la prochaine valeur pas rayer (3) et raye tout les multiple qui reste sur le tableau. On continue ainsi de suite jusqu'à qu'il y a plus de valeur à prendre dans le tableau.