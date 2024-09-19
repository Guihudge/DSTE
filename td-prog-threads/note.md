# Programmation threads
## Exo 1
### Quel est le rôle du crible d’Erathostène ?
Le crible d’Eratosthène est une méthode permettant de calculer les nombres premiers de 2 à N, où N est fixé par l'utilisateur.

### Expliquer son fonctionnement
On commence par créer un tableau de 2 à N. Puis on raye tous les multiples de 2 jusqu'à arriver à la fin du tableau. On prend ensuite la prochaine valeur non rayée (ce qui représente le prochain nombre premier) et on raye tous les multiples de ce nombre qui reste sur le tableau. On continue ainsi de suite jusqu'à qu'il y a plus de valeur à prendre dans le tableau.