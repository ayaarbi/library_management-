# L'éxecution des fonction ci-dessous affiche des questions, si vous voulez le programme exécutera la tâche en question alors repondez par "oui", sion par "non"
# S'il vous plaît, pour comprendre mieux comment fonctionne le programme, lisez-vous le fichier PDF attentivement et qui se trouve dans le répertoire de travail



from gestion import *    #Pour importer les fonctions existant dans le fichier gestion.py

#Une fonction permet la gestion des clients de notre bibliothèque
gestion_client()

#Une fonction permet la gestion des ressources de la bibliothèque
gestion_bibliotheque()

#Une fonction permet la gestion des abonnements des clients
gestion_abonnement()

#Une fonction permet la gestion des emprunts des clients de notre bibliothèque
gestion_emprunt()

#Une fonction permet la gestion des autres choses: le Blacklist, les notifications, les rentrées/mois et les statistiques
gestion()