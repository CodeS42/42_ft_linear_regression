# Partie obligatoire

Le but du projet est de créer deux programmes : 

- Le premier doit être capable d’estimer le prix d’une voiture en fonction de son kilométrage, à l’aide d’un modèle de régression linéaire simple (= une seule variable explicative).
- Le second est le programme d’entraînement du modèle. Il va implémenter la descente de gradient (= l’algorithme d’apprentissage), calculer les valeurs des paramètres que le premier programme utilise pour son calcul à partir du fichier data.csv qui nous est fourni, et les stocker dans un fichier.

Ce dernier contient 2 colonnes, nous donnant des informations sur plusieurs voitures:

- km : leur kilométrage
- price : leur prix

Il est important de comprendre que ces données se rapprochent de données réelles, et qu’elles ne suivent pas une relation linéaire parfaite, en raison de l’existence d’autres facteurs, tels que la marque, l’état de la voiture, etc.

Le but n’est donc pas de faire en sorte que notre algorithme soit capable d’estimer le prix exact de chaque voiture, mais de trouver, en se basant sur ces données, la droite qui minimise l’erreur globale sur l’estimation du prix de toutes les voitures.

Les estimations fournies par le modèle seront, quant à elles, linéaires en fonction du kilométrage, puisqu’elles suivent une droite.

---

# Partie bonus

Il y a 3 bonus :

- Le premier consiste à représenter les données du fichier data.csv dans un graphique, sous forme de nuages de points.
- Le second nous demande d’ajouter la droite correspondant aux estimations du modèle dans ce même graphique.
- Le dernier vise à créer un programme capable de  calculer la précision de notre algorithme.


---

# Programme n°1

Ce programme va :

- Demander à l’utilisateur de fournir un input : le kilométrage d’une voiture.
- Lire le fichier dans lequel se trouvent theta0 et theta1.
    
    → Si le fichier n’existe pas, on garde leur valeur de base : theta0 = 0 et theta1 = 0.
    
- Estimer le prix de cette voiture grâce au modèle de régression linéaire.

Sans le programme n° 2, les estimations de ce programme n’ont donc aucune réelle valeur, car il ne connait ni la valeur de theta0 ni celle de theta1.


## Explications du calcul

### Le modèle de régression linéaire

**Définition :**

Le modèle de régression linéaire est un calcul qui va permettre de représenter la relation entre une variable explicative (ici, le kilométrage) et une valeur cible (le prix estimé).

Ici, il s’agit d’une régression linéaire simple : il n’y a qu’une seule variable explicative.

**Calcul :**

```jsx
y_hat = theta0 + (theta1 * x)
```

- y_hat : la valeur prédite
    → le prix estimé
    
- theta0 : le biais
    → le prix estimé si le kilométrage était à 0
    
- theta1 : le poids
    → la variation du prix estimé de la voiture à chaque unité de kilométrage
    
- x : la variable explicative
    → le kilométrage