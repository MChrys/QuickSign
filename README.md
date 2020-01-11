# QuickSign
Livrable



## 1. Exécution du projet
  
  - installez docker, docker-compose et git
  - clonez le répertoire avec la commmande `git clone https://github.com/MChrys/QuickSign.git`
  
Dans le répertoir du projet, montez l'image avec la `docker-compose build`, cette étape est à réaliser seulement la première fois.

Pour lancer l'image utilisez simplement `docker-compose build`

## 2. Ouverture des applications 

Une fois l'image lancée vous avez accès:

au serveur Mlflow via l'adresse : <br>
  [https//:127.0.0.1:5000](https//:127.0.0.1:5000)

au Jupyter notebook via : <br>
  [https//:127.0.0.1:8887](https//:127.0.0.1:8887)

## 3. Lancement d'une run du project tensorflow

![run](/img/premier_run.PNG)

  - ouvrez le notebook `GUI_QuickSign.ipynb`
  - executez la première cellule via le raccourci `SHIFT + ENTRY` si vous voyer ce message
    

![run](/img/run_livrable.PNG)

Via l'interface GUI qui apparaît faites varier les deux paramètre, si vous en souhaitez de différent que ceux par défault
Cliquez simplement sur le boutton  `RUN`

Dans la page du serveur ML vous constaterez le résulat de la run du projet dans l'expérience `QuickSign-tensorflow`

## 4. Evaluer le code avec pylint

ouvrez l'onglet `pylint eval` et cliquez sur le boutton `rating`

![run](/img/rating_livrable.PNG)

A la fin des logging on obtiens un score sur 10

## 5. l'interface

  - le boutton `hiding / display code` permet d'afficher ou de masquer le code
  - le lien à côté de `show off/on warning` permet d'afficher ou de cacher les messages d'alert rose
