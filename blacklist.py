import json
import datetime

with open("blacklist.json") as f:
    file=json.load(f)
with open('empreint.json') as f2:
    file2 = json.load(f2)

blacklist=file["blacklist"]
emprunt=file2["empreint"]


#Fonction pour ajouter un client à blacklist
def ajout_bl():
    """
    Cette fonction permet d'ajouter un client dans la blackliste
    """
    mntenant = datetime.datetime.now()
    for emp in emprunt: #Parcourt la liste des empreints
        date_retour=emp["date limite de retour"]  #Extraire pour chaque empreint sa date de retour
        date=datetime.datetime.strptime(date_retour,"%d/%m/%Y")
        diff= mntenant-date
        d=diff.days
        if d> 0: #Si la date de retour dépasse la date d'aujourd'hui alors on ajoute le client à la blacklist
            cin=emp["cin de client"]
            nv_bl = {
                "cin de client": cin,
                "jours de non empreints": d  #Le client ne peut pas empreinter des nouvelles entités que aprés d jours
            }
            blacklist.append(nv_bl)
            with open("blacklist.json", "w") as f:
                json.dump(file, f)

# Fonction pour l'affichage de black list
def affichage_bl():
    """
    Cette fonction permet d'afficher la liste du Blacklist
    """
    for bl in blacklist:
        res = "\ncin de client: {} \njours de non empreints: {} \n"
        print(res.format(bl["cin de client"], bl["jours de non empreints"]))