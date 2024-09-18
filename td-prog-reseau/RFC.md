Status de ce mémo :
Ce mémo est en état de brouillon. 

Résumé :
Ce mémo présente le fonctionnement d'une version très simplifié de finger.

Table of Contents

## 1. Introduction
Cette RFC à pour objectif de parler d'une version très allégée de finger (présenter dans les RFC 1288 et 742). Plus précisément, nous allons communiquer avec un serveur en lui envoyant un nom d'utilisateur et il nous renvoie le nom correspondant. Toutes les communications seront en TCP.

## 2. Utilisation du protocole
### 2.1. Flot des évènements
Les échanges commencent avec une demande d'ouverture de connexion TCP au serveur. Cette demande est envoyée par le client. Si la demande est acceptée, le serveur attend de recevoir le nom d'utilisateur. Une fois le nom reçu, le serveur revoit les prénoms s'il le connaît ou `unknown` dans le cas contraire. Le serveur termine en fermant la connexion avec le client.

### 2.2. Data format
Les noms d'utilisateur sont envoyés en ASCII, à travers une connexion TCP. La taille par défaut des buffers d'envoi et de réception est de 50 pour le serveur et de 100 pour le client.

### 2.3. Spécification des demandes
Nous avons choisi l'interface suivante pour la ligne de commande du client :

`finger-client username hostname [port]`

Pour les champs variable :
- `username` : le nom que l'on va demander au serveur.
- `hostname` : le nom d'hôte de la machine visé.
- `port` : un numéro de port si l'on souhaite en utiliser un autre que celui par défaut (4242).

### 2.4. Comportement
Le comportement varie en fonction des paramètres spécifiés par l'utilisateur sur la ligne de commande. C'est principalement le nom d'hôte et le nom d'utilisateur.

### 2.5. Réponse
La réponse à une taille maximum de 100 caractères par défaut. Les caractères sont encodés en ASCII.

## 3. Sécurité
Le protocole n'embarque aucune sécurité.

## 4. Exemples
Demande du nom de l'utilisateur `Grominet`:
```
$ ./finger-client Grominet localhost                                                                                                        14:15:14
Summary:
Hotname: localhost (127.0.0.1)
Username: Grominet
Port: 4242

First name: Titi
```

Demande du nom de l'utilisateur `Jean` (qui n'existe pas sur le serveur) :
```
$ ./finger-client Jean localhost
Summary:
Hotname: localhost (127.0.0.1)
Username: Jean
Port: 4242

First name: Unknown
```

## 6. Considérations de sécurité
Toutes les informations sont échangées en clair à travers le réseau, de plus, le serveur n'effectue aucune forme d'identification sur la personne qui réalise la requête.

## 7. Autheur
Guillaume Dindart