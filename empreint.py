import json
import datetime

with open('empreint.json') as f:
    file = json.load(f)
with open("bibliotheque.json") as f2:
    file2=json.load(f2)
with open("abonnement.json") as f3:
    file3=json.load(f3)

emprunt=file["empreint"]
livres= file2["livres"]
magazines=file2["magazines"]
dvds=file2["dvds"]
abnment=file3["abonnement"]

#Fonction pour ajouter un nouvel empreint
def ajout_emp():
    """
    Cette fonction permet d'ajouter un nouveau empreint dans la liste
    """
    while True:
        cin=input("Donner le cin d'utilisateur: ")
        if len(cin)==8:
            break
    for abn in abnment:
        if abn["cin de owner"]==cin:
            tpe=abn["type"]
            nbr=str(len(emprunt)+1)
            def emp():
                """
                Cette fonction permet de fournir une liste des entités dont le client ont choisis selon le type de son abonnement
                """
                n = int(input("Donner le nombres des entites que ce client a empuntes: ")) #On stocke dans cette variable le nombre des entités que le client a empreinté
                if abn["type"] == "normal": #si l'abonnement du client est de type normal, on procéde comme suivant
                    entite = [""]*3
                    i = 1
                    if n > 3:
                        print("Impossibe: ce client a un abonnement normal, il n'emprunt que 3 entites au plus")
                    else:
                        while i <= n:
                            ent = input(f'Donner le titre de {i}ime entite: ')
                            entite[i-1] = ent
                            i += 1
                        for elt in entite:
                            if elt=="":
                                entite.remove(elt)
                        entite.pop(-1)
                    return entite
                elif abn["type"] == "premium": #si l'abonnement du client est de type premium, on procéde comme suivant
                    entite = [""]*5
                    i = 1
                    if n > 5:
                        print("Impossibe: ce client a un abonnement premium, il n'emprunt que 5 entites au plus")
                    else:
                        while i <= n:
                            ent = input(f"Donner le titre de {i}ime entite: ")
                            entite[i-1] = ent
                            i += 1
                        for elt in entite:
                            if elt=="":
                                entite.remove(elt)
                        entite.pop(-1)
                    return entite
            emprt=emp()
            d_emp = datetime.datetime.now()
            date_emp=d_emp.strftime("%d/%m/%Y") #La date de nouveau empreint coïcide avec la date d'aujourd'hui
            date_limite = (d_emp + datetime.timedelta(days=15)).strftime("%d/%m/%Y") #La date limite sera aprés 15 jours de date d'empreint
            nv_emp = {
                "cin de client": cin,
                "numero d'empreint": nbr,
                "type d'abonnement": tpe,
                "entites": emprt,
                "date de l'empreint": date_emp,
                "date limite de retour": date_limite
            }
            emprunt.append(nv_emp)
            with open("empreint.json", "w") as f:
                json.dump(file, f)

# Fonction pour supprimer un empreint
def supprime_emp():
    """
    Cette fonction permet de supprimer un empreint de la liste
    """
    nbr = input("Donner le nombre de l'empreint pour supprimer: ")
    for emp in emprunt:
        if emp["numero d'empreint"] == nbr:
            emprunt.remove(emp)
            with open("empreint.json", "w") as f:
                json.dump(file,f)
            break

# Fonction pour afficher les informations d'un empreint
def affiche_emp():
    """
    Cette fonction permet afficher les informations d'un emprient
    """
    nbr = input("Donner le nombre de l'empreint à afficher: ")
    for emp in emprunt:
        if emp["numero d'empreint"] == nbr:
            res = "\ncin de client: {} \nnumero d'empreint: {} \ntype d'abonnement: {} \nentites: {} \ndate de l'empreint: {} \ndate limite de retour: {} \n"
            print(res.format(emp["cin de client"], emp["numero d'empreint"], emp["type d'abonnement"], emp["entites"], emp["date de l'empreint"], emp["date limite de retour"]))

# Fonction pour afficher la liste des empreints
def affichage_emp():
    """
    Cette fonction permet d'afficher la liste des empreints
    """
    for emp in emprunt:
        res = "\ncin de client: {} \nnumero d'empreint: {} \ntype d'abonnement: {} \nentites: {} \ndate de l'empreint: {} \ndate limite de retour: {} \n"
        print(res.format(emp["cin de client"], emp["numero d'empreint"], emp["type d'abonnement"], emp["entites"],emp["date de l'empreint"], emp["date limite de retour"]))
