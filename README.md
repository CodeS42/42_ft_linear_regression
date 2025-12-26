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


## Explication du calcul

### Le modèle de régression linéaire

**Définition :**

Le modèle de régression linéaire est un calcul qui va permettre de représenter la relation entre une variable explicative (ici, le kilométrage) et une valeur cible (le prix estimé).

Ici, il s’agit d’une régression linéaire simple : il n’y a qu’une seule variable explicative.

**Calcul :**

```jsx
estimated_price = theta0 + (theta1 * mileage)
```

- theta0 : le biais
    
    → le prix estimé si le kilométrage était à 0
    
- theta1 : le poids
    
    → la variation du prix estimé de la voiture à chaque unité de kilométrage
    

On multiplie le kilométrage à la variation du prix pour obtenir la variation totale pour ce nombre de kilométrage. Puis on ajoute celle-ci au prix de départ estimé de la voiture pour obtenir le prix estimé par rapport à son kilométrage.


---

# Programme n°2

Ce programme va :

- Récupérer le contenu du data.csv.
- Normaliser les prix et les kilométrages.
    
    → Cela permet, lors du calcul des corrections, d’obtenir des nombres plus petits, et d’améliorer la convergence. Avec des nombres trop grands, les corrections pourraient être trop grandes, et la convergence vers le minimum de l’erreur pourrait ne jamais être atteinte.
    
- Définir un learning rate (= le facteur multiplicatif qui controle l’amplitude de la correction appliquée aux thetas).
    
    → Sans learning rate (ou si celui-ci est trop élevé), les corrections appliquées pourraient être trop grandes, et empêcher la convergence vers le minimum de l’erreur.
    
- Initialiser les thetas à 0, car on ne connait pas encore leur valeur.
- Lancer la boucle d’apprentissage :
    - Utiliser le modèle de régression linéaire pour calculer les prix estimés pour chaque kilométrage du data.csv.
    - Calculer l’erreur entre chaque prix estimé et chaque prix du data.csv.
    - Calculer la correction du theta0 et celle du theta1.
    - Mettre à jour simultanément theta0 et theta1.
        
        → S’ils ne sont pas mis à jour simultanément, les résultats pourraient être faussés.
        
    - Quitter la boucle si la correction des thetas est suffisamment faible.
        
        → Plus l’erreur est faible, plus la correction l’est aussi.
        
- Dénormaliser theta0 et theta1, pour retrouver des valeurs réalistes qui nous permettront d’obtenir le véritable prix estimé.
- Enregistrer les thetas dans un fichier pour que le programme n°1 puisse les récupérer.
- Afficher un graphique contenant le nuage de points et la droite afin de visualiser la tendance moyenne des prix des voitures en fonction de leur kilométrage (bonus).


## Explication des calculs

### Le modèle de régression linéaire

→ voir Programme n°1

### L’erreur

**Calcul :**

```jsx
error = estimated_price - price
```

On soustrait le prix au prix estimé par le modèle de régression linéaire pour obtenir l’erreur.

Si l’erreur est positive, le prix estimé est trop grand. Si elle est négative, le prix estimé est trop petit.

### Le gradient partiel

*(Ces calculs nous sont donnés dans le sujet)*

**Calculs :**

```jsx
correction_theta0 = learning_rate * (1/m) * sum(errors)
correction_theta1 = learning_rate * (1/m) * sum(errors * mileages)
```

m : nombre total de voitures

Gradients partiels:

- (1/m) * sum(errors)
    
    → Moyenne des erreurs pour theta0.
    
- (1/m) * sum(errors * mileages)
    
    → Moyenne des erreurs multipliées par les kilométrages pour theta1.
    

On calcule les gradients partiels de theta0 et theta1.

→ On obtient la correction 

On multiplie ces moyennes par le learning rate pour en appliquer une seule partie.

### La descente de gradient

**Calculs :**

```jsx
theta0 = theta0 - correction_theta0
theta1 = theta1 - correction_theta1
```

On applique la correction calculée aux thetas en les soustrayant à ces derniers.


---

# Programme bonus

Le bonus visant à réaliser un programme démontrant la précision de notre algorithme est assez libre. 

J’ai donc décidé de créer un programme supplémentaire qui va :

- Récupérer les données du fichier contenant les thetas.
- Récupérer les données de data.csv.
- Faire l’estimation du prix des voitures du data.csv.
- Calculer la moyenne des erreurs absolues et la moyenne des prix réels pour calculer le pourcentage de précision.
- Puis calculer et afficher la précision de mon algorithme en pourcentage.


## Explication des calculs

### Le modèle de régression linéaire

→ Voir Programme n°1

### La moyenne des erreurs absolues

**Calcul :**

```jsx
mean_absolute_error = sum(abs(ep - p) for ep, p in zip(estimated_prices, prices)) / m
```

m : nombre total de voitures

On fait la somme des erreurs absolues, puis on la divise par le nombre de voitures.

→ L’erreur absolue nous permet d’ignorer le signe de chaque erreur, qui, dans le calcul d’une moyenne, fausserait le résultat en faisant baisser la somme avec des erreurs négatives.

### La moyenne des prix réels

**Calcul :**

```jsx
average_price = sum(prices) / m
```

m : nombre total de voitures

On divise la somme des prix réels par le nombre de voitures pour obtenir la moyenne des prix.

### Le pourcentage

**Calcul :**

```jsx
accuracy_percentage = 100 * (1 - mean_absolute_error / average_prices)
```

On divise la moyenne des erreurs absolues par la moyenne des prix réels, on soustrait ce résultat à 1, puis on multiplie le tout par 100 pour obtenir le pourcentage de précision de notre algorithme.

→ “1 -” est indispensable pour afficher le pourcentage de précision. Sans lui, le calcul donnerait le pourcentage d’erreur.