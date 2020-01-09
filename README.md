# QuickSign
Livrable



# 1. Execution du projet
  
  - installez docker, docker-compose et git
  - clonez le répertoire avec la commmande `git clone https://github.com/MChrys/QuickSign.git`
  
Dans le répertoir du projet, montez l'image avec la `docker-compose build`, c'est étape est à réaliser seulement la première fois.

Pour lancer l'image utilisez simplement `docker-compose build`

# 2. Ouverture des applications 

Une fois l'image lancé vous avez accés:

au serveur Mlflow via l'adresse : <br>
  [https//:127.0.0.1:5000](https//:127.0.0.1:5000)

au Jupyter notebook via : <br>
  [https//:127.0.0.1:8887](https//:127.0.0.1:8887)

# 3. Lancement d'une run du project tensorflow

  - ouvrez le notebook `GUI_QuickSign.ipynb`
  - executez les deux premère cellule via le raccourci `SHIFT + ENTRY`

[run](/img/run_livrable.png)

Via l'interface GUI qui apparait faites varier les deux paramètre, si vous en souhaitez de différent que ceux par défault
Cliquez simplement sur le boutton  `RUN`

Dans la page du serveur ML vous constaterez le resulat de la run du projet dans l'expérience `QuickSign-tensorflow`
