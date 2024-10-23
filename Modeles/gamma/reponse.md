# Modèles GAMMA

## Exercice 1
### a.1
V: (#v, i, v)

M_0 = U i=1,n1 {1, i, v1[i]} + U i=1,n2 {2, i, v2[i]}
R(X,Y) = (X.#v != Y.#v) and (X.i == Y.i)
A(X,Y) = {(3,i,X.v + Y.v)}

## a.2
On peut modifier le programme de la manière suivante pour supprimer des valeurs:
V: (i, v)

M_0 = U i=1,n1 {i, v1[i]} + U i=1,n2 {i, v2[i]}
R(X,Y) = (X.i == Y.i)
A(X,Y) = {(i, X.v + Y.v)}

On peut donc supprimer le numéro du vecteur.


## b

## c
V: (i, v)

M_0 = pour chaque vecteur v contenant n élément : M_0 += U i=1,n {i,v[i]}
R(X,Y) = (X.i == Y.i)
A(X,Y) = {(i, X.v + Y.v)}

## Exo 2
### a
V: (i, l, m)

M_0 = U i=0,2n {i, m[i], 1}

R(X) = X.m = 1
A(X) = Si X.i > n alors {i-n, X.l, 0} sinon {i+n, X.l, 0}

M_F = U i=0,2n {i, l, 0}

### b

## Exo 3
Image de taille ix,iy

V: (x, y, v, m)

M_0 = U i = 0, ix (U j=0,iy ({i,j,img[i,j], 1}))

R(X) = X.m = 1
A(X) = {X.x, X.y, not v, 0}

M_F = U i = 0, ix (U j=0,iy ({i,j,img[i,j], 0}))


## Exo 5

### 2
Tableau de taille n

V: (i,v)

M_0 = U i=0,n (i,v[i])

R(X,Y) = X.i > Y.i and X.v < Y.v
A(X,Y) = {X.i, Y.v}, {Y.i, X.v}

NB premier:

V(v)
M_0 = U i=2,30 (i)

R(X,Y) = Y.v != 1 and X.v%Y.v == 0
A(X,Y) = Y.v

## Exo 6

Vecteur 1 de taille n1
Vecteur 2 de taille n2
avec n1 = n2

V: (i,v)

M_0 = U i=0,n1 (i,v1[i]) + U i=0,n2 (i,v2[i])

R1(X,Y) = X.i = Y.i and X.i != -1 and Y.i != -1
A(X,Y) = {-1, X.v * Y.v}

R2(X,Y) = X != Y and X.i == -1 et Y.i == -1
R2(X,Y) = {-1, X.v + Y.v}

Fin si il n'y a plus que 1 molécule.
