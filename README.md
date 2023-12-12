## ProjetData354

### **Contexte du Projet : Construction d'un Modèle de Machine Learning pour la Détection de Phishing**


**Objectifs du Projet:**

- Analyse des Données : Comprendre la nature des données disponibles, identifier les caractéristiques pertinentes et établir des tendances et des relations potentielles.
  
- Nettoyage des Données : Prétraiter les données pour éliminer les valeurs manquantes, les duplications et tout bruit indésirable, garantissant ainsi la qualité des données pour l'entraînement du modèle.
  
- Création de Features Appropriés : Développer des caractéristiques pertinentes pour la détection de phishing, en tenant compte des différentes méthodes et techniques utilisées par les cybercriminels.
  
- Comparaison de Modèles : Évaluer au moins trois modèles de machine learning pour déterminer celui qui présente les meilleures performances dans la détection de phishing.
  
- Prédiction du Label pour le Fichier de Soumission : Appliquer le modèle entraîné pour prédire les labels de phishing sur un ensemble de données distinct pour évaluer la généralisation du modèle.

Optionnel : Déploiement d'une API :
Pour une utilisation pratique, le projet pourrait inclure le développement d'une API (Interface de Programmation d'Applications) permettant le déploiement du modèle de détection de phishing. Cela offrirait la possibilité d'intégrer le modèle dans divers systèmes et applications pour une protection en temps réel contre les attaques de phishing

### I)   Qu'est ce que le phising
### II)  Fichiers essentiels
### III) Structuration du projet
### IV)  Perspectives


### D'abord posons les jalons et donnons quelques définition afin que ce projet soit compris dans son ensemble.

## I) Qu'est ce le Phising

**Définition du phishing** 
Le phishing constitue une attaque sophistiquée de cybercriminalité visant à induire en erreur les individus et à les inciter à divulguer des informations sensibles, telles que des identifiants, mots de passe et données financières.

**Objectifs du Phishing**

- Vol d'identifiants : noms d'utilisateur, mots de passe, informations de carte de crédit.
- Propagation de logiciels malveillants.
- Accès non autorisé à des systèmes sensibles.

**Méthodes de Phishing**
- E-mails frauduleux : Utilisation de messages simulés pour inciter les destinataires à cliquer sur des liens URL malveillants ou à télécharger des fichiers dangereux.
- Sites Web de phishing : Création de faux sites ressemblant à des sites officiels pour collecter des informations sensibles.
- Hameçonnage téléphonique (vishing) : Manipulation des individus par téléphone pour obtenir des informations confidentielles.

**Techniques d'Ingénierie Sociale**

- Création de faux sites Web : copie de sites officiels pour induire en erreur.
- Utilisation de noms de domaine similaires : des URL proches des sites légitimes.
- Utilisation de logos et de graphiques authentiques : pour renforcer la crédibilité.

**Reconnaître les Signes d'une Attaque de Phishing**

- Vérification de l'expéditeur de l'e-mail.
- Analyse de l'URL : s'assurer qu'elle est correcte et sécurisée (https).
- Méfiance envers les demandes d'informations sensibles par e-mail.

**Prévention et Protection**

- Formation à la sensibilisation : éduquer les utilisateurs sur les signes de phishing.
- Utilisation de filtres anti-phishing : outils pour détecter et bloquer les e-mails de phishing.
- Mises à jour régulières des logiciels de sécurité.

## II)  Fichiers essentiels

- Notebook [ici](https://github.com/Fotiemb/ProjetData354/blob/main/DetectionDePhising.ipynb)
- plateforme développé pour tester le modèle: http://fotiemb.pythonanywhere.com/ vous trouverez le code source [ci-joint](https://github.com/Fotiemb/ProjetData354/tree/main/PhinsingPredictWeb)
- API: [ici](https://github.com/Fotiemb/ProjetData354/tree/main/API_ForDeployment)

## III) Structuration du projet

### Reponses aux Objectifs

`Note:` Se référer au notebook [ici](https://github.com/Fotiemb/ProjetData354/blob/main/DetectionDePhising.ipynb) Pour mieux comprendre notre approche.

  **Analyse du jeu de données**
  
  Nous avons 23523 entrées uniques. Il y a deux colonnes, celle de URL et de la colonne d'étiquette qui est le label avec 2 catégories:
  
  `legit`: Ce qui signifie que les URL ne contiennent pas d'éléments malveillants et que ce site n'est pas un phishing.
  
  `fishing`: Ce qui signifie que les URL contiennent des éléments malveillants et que ce site est un site de phishing.

Il n'y a aucune valeur manquante dans l'ensemble de données.

 
  **prétraitement:**
  
  Nous avons opté pour une approche dans le contexte du texte mining.

Nous avons créé une fonction appelée preprocess_initial qui permet d'effectuer le prétraitement sur l'ensemble de nos URLs. Cette fonction réalise la tokenization et la racinisation initiales sur une URL. Elle utilise un tokenizer pour diviser l'URL en mots, un stemmer pour réduire les mots à leur racine, puis supprime les stopwords spécifiques aux URLs. Enfin, elle concatène les mots résultants pour former une version traitée de l'URL.

  **Création de Features Appropriées:**

Nous avons transformé nos données d'URL en une matrice TF-IDF pour la création de caractéristiques (features).

**Comparaison de Modèles:**

Nous avons comparé trois modèles en utilisant différentes techniques de machine learning. Pour plus de détails, veuillez vous référer au notebook.

**Prédiction du Label pour le Fichier de Soumission:**

Nous avons fait les prédictions sur les données de soumissions pour voir si notre moèle arrive à bien généraliser sur de nouvelles données.

**Mise en place d'une API**

Nous avons mis en place une API grâce à FastAPI suivez les étapes suivantes pour la déployer en local

```
https://github.com/Fotiemb/ProjetData354.git
```
```
cd API_ForDeployment
```

```
uvicorn main:app --reload
```
Après ces étapes tapez dans votre navigateur l'url suivante:

```
http://127.0.0.1:8000/docs
```
Et voilà !

![image](https://github.com/Fotiemb/ProjetData354/assets/99336213/0ee8bc65-ff87-447b-bcef-7b21a240debe)


**Déploiement d'une APP**

Nous avons intégré le modèle à une application (basique) en production entre griffe.
Nous vous fournissons des données test que vous pourriez utiliser pour voir le comportement de l'application.

données:
`URL normale(pas phising):` 
```
http://fotiemb.pythonanywhere.com/
```
`URL anormale(phising)`: 
```
http://yeniik.com.tr/wp-admin/js/login.alibaba.com/login.jsp.php
```

lien vers l'application: http://fotiemb.pythonanywhere.com/

## IV)  Perspectives



