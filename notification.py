import json
import datetime

with open('empreint.json') as f:
    file = json.load(f)

emprunt=file["empreint"]

duree=datetime.timedelta(hours=24)
date=datetime.datetime.now()

def notification():
    """
    Cette fonction permet d'afficher la liste des notifications concernant les clients qui doit retourner lerurs empreintes
    """
    for emp in emprunt:
        # Convertir la date limite de retour de la chaîne en objet datetime
        date_limite = datetime.datetime.strptime(emp["date limite de retour"], '%d/%m/%Y')
        # Calculer la différence entre la date limite de retour et la date et l'heure actuelles
        diff = date_limite - date
        if diff < duree:
            res="Notifier le client {} qu'il doit retourner ses emprients {} avant demain qui coincide avec la date limite de retour {}"
            print(res.format(emp['cin de client'],emp["numero d'empreint"],emp['date limite de retour']))


