import json

with open("historique.json") as f:
    file=json.load(f)
with open("empreint.json") as f1:
    file1=json.load(f1)
with open("client.json") as f2:
    file2=json.load(f2)
with open("abonnement.json") as f3:
    file3=json.load(f3)

historique=file["historique"]
empreint=file1["empreint"]
clients=file2["clients"]
abonment=file3["abonnement"]

#Fonction pour ajouter l'historique d'un client au fichier de l'historique
def ajout_hist():
    """
    Cette fonction permet d'ajouter l'hitorique d'un client à la liste des historiques
    """
    def existe(cin):
        """
        Cette fonction permet de vérifier si un client existe dans la liste des clients
        """
        for client in clients:
            if cin in client.values():
                return True
        return False

    while True:
        cin=input("Donner le cin de client: ")
        if existe(cin):
            break
    empreints=[]
    for emp in empreint:
        if emp["cin de client"]==cin:
            empreints.append(emp["numero d'empreint"])
    for abn in abonment:
        if abn["cin de owner"]==cin:
            nb_abn=abn["numero d'abonnement"]
    while True:
        try:
            renvelment = int(input("Donner le nombre de fois que ce client a renouveller son abonnement: "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour le renouvellement.")

    while True:
        try:
            reptation = int(input("Donner le nombre de fois que ce client a été black listé: "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour la réputation.")
    nv_hist = {
        "cin de client": cin,
        "empreints": empreints,
        "abonnement": nb_abn,
        "renouvellement": str(renvelment),
        "reputation": str(reptation)
    }
    historique.append(nv_hist)
    with open("historique.json","w") as f:
        json.dump(file,f)

# Fonction pour afficher l'historique d'un client
def affiche_hist():
    """
    Cette fonction permet d'afficher l'historique d'un client donné
    """
    cin = input("Donner le cin de client que vous voulez afficher son historique: ")
    for hist in historique:
        if hist["cin de client"] == cin:
            res = "\ncin de client: {} \nempreints: {} \nabonnement: {}\nrenouvellement: {} \nreputation: {} \n"
            print(res.format(hist["cin de client"], hist["empreints"], hist["abonnement"], hist["renouvellement"], hist["reputation"]))

# Fonction pour afficher la liste des historiques
def affichage_hist():
    """
    Cette fonction permet d'afficher la liste des historiques
    """
    for hist in historique:
        res = "\ncin de client: {} \nempreints: {} \nabonnement: {}\nrenouvellement: {} \nreputation: {} \n"
        print(res.format(hist["cin de client"], hist["empreints"], hist["abonnement"], hist["renouvellement"], hist["reputation"]))


