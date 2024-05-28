import json
import datetime
from dateutil.relativedelta import relativedelta

with open("abonnement.json") as f:
    file = json.load(f)
with open("client.json") as f1:
    file1 =json.load(f1)

abnment = file["abonnement"]
clients= file1["clients"]


#Fonction pour ajouter un nouvel abonnement
def ajout_abn():
    """
    Cette fonction permet d'ajouter un nouvel abonnement à la liste
    """
    while True:
        cin=input("Donner le cin d'utilisateur: ")
        if len(cin)==8:
            break
    for client in clients:
        if client["cin"]==cin:
            nbr=str(len(abnment)+1)
            while True:
                tpe=input("Donner le type de l'abonnement (normal/premium): ")
                if tpe=="normal" or tpe=="premium" :
                    break
            d_crtion = datetime.datetime.now()
            date_crtion=d_crtion.strftime("%d/%m/%Y") #La date de création d'un nouvel abonnement coîncide avec la date d'aujourd'hui
            date_rnvmt = (d_crtion + relativedelta(years=1)).strftime("%d/%m/%Y") #La date de renouvellement doit être aprés une ennée du date de création
            nv_abnmt={
                "cin de owner": client["cin"],
                "numero d'abonnement": nbr,
                "date de creation": date_crtion,
                "date de renouvellement": date_rnvmt,
                "type": tpe
            }
            abnment.append(nv_abnmt)
            with open("abonnement.json","w") as f:
                json.dump(file, f)


#Fonction pour supprimer un abonnement
def supprime_abn():
    """
    Cette fonction permet de supprimer un abonnement
    """
    nbr=input("Donner le nombre de l'abonnement pour supprimer: ")
    for abn in abnment:
        if abn["numero d'abonnement"]==nbr:
            abnment.remove(abn)
            with open("abonnement.json","w") as f:
                json.dump(file,f)
            break


#Fonction pour afficher les informations d'un abonnement
def affiche_abn():
    """
    Cette fonction permet d'afficher les informations d'un abonnement donné
    """
    nbr = input("Donner le nombre de l'abonnement à afficher: ")
    for abn in abnment:
        if abn["numero d'abonnement"] == nbr:
            res="\ncin de owner: {} \nnumero d'abonnement: {} \ndate de creation: {} \ndate de renouvellement: {} \ntype: {} \n"
            print(res.format(abn["cin de owner"],abn["numero d'abonnement"],abn["date de creation"],abn["date de renouvellement"],abn["type"]))

 # Fonction pour afficher la liste des abonnements
def affichage_abn():
    """
    Cette fonction permet d'afficher la liste des abonnements
    """
    for abn in abnment:
        res = "\ncin de owner: {} \nnumero d'abonnement: {} \ndate de creation: {} \ndate de renouvellement: {} \ntype: {} \n"
        print(res.format(abn["cin de owner"], abn["numero d'abonnement"], abn["date de creation"],abn["date de renouvellement"], abn["type"]))
