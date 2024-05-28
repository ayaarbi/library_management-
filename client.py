import json

with open("client.json") as f:
    file =json.load(f)

clients= file["clients"]


# Fonction pour ajouter un nouveau client
def ajouter_client():
    """
    Cette fonction permet d'ajouter un nouveau client
    """
    #Le client doit saisir ces informations en respectant les contraintes
    while True:
        nom = input("Donner le nom de client: ")
        if nom.isalpha() or nom.__contains__(" "): #On accepte les noms qui ont comme caractére un espace " " (par example le nom: "ben youssef" qui contient un espace)
            break
    while True:
        prenom = input("Donner le prénom de client: ")
        if prenom.isalpha() or prenom.__contains__(" "): #On accepte les prénoms qui ont comme caractére un espace " " (par example le prénom: "mohamed ali" qui contient un espace)
            break
    while True:
        cin = input("Donner le cin de client: ")
        if len(cin) == 8:
            break
    while True:
        genre = input("Donner le genre de client (homme/femme): ")
        if genre == "femme" or genre == "homme":
            break
    while True:
        date_naissance = input("Donner la date de naissance de client (sous la forme jj/mm/aaaa): ")
        if 0 < int(date_naissance[:2]) <= 31 and 0 < int(date_naissance[3:5]) <= 12 and len(date_naissance[6:]) == 4 and date_naissance[2] == date_naissance[5] == "/":
            break
    adresse = input("Donner l'adresse de client: ")
    while True:
        telephone = input("Donner le numéro de téléphone de client: ")
        if telephone.isdigit() or telephone.__contains__("+") or telephone.__contains__("-") or telephone.__contains__(" "):
            break
    nv_client = {
        "nom": nom,
        "prenom": prenom,
        "cin": cin,
        "genre": genre,
        "date_naissance": date_naissance,
        "adresse": adresse,
        "telephone": telephone
    }
    clients.append(nv_client)
    with open('client.json', 'w') as f:
        json.dump(file, f)

# Fonction pour supprimer un client
def supprime_client():
    """
    Cette fonction permet de supprimer un client de la liste
    """
    cin = input("Donner le cin de client que vous voulez le supprimer: ")
    for client in clients:
        try:
            if client["cin"] == cin:  # On cherche le client à supprimer en utilisant son cin
                clients.remove(client)
                with open('client.json', 'w') as f:
                    json.dump(file, f)
                break
        except:
            print("Ce client n'existe pas")

# Fonction pour modifier les informations d'un client
def modifier_client():
    """
    Cette fonction permet de modifier les informations personnelles d'un client
    """
    cin = input("Donner le cin de client que vous voulez modifier ses informations: ")
    for client in clients:
        if client["cin"] == cin:
            # Le client peut changer uniquement ces informations
            while True:
                nom = input("Donner le nom de client: ")
                if nom.isalpha() or nom.__contains__(" "):
                    break
            while True:
                prenom = input("Donner le prénom de client: ")
                if prenom.isalpha() or prenom.__contains__(" "):
                    break
            adresse = input("Donner la nouvelle adresse de client: ")
            while True:
                telephone = input("Donner le numéro de téléphone de client: ")
                if telephone.isdigit() or telephone.__contains__("+") or telephone.__contains__("-") or telephone.__contains__(" "):
                    break
            md_client = {
                "nom": nom,
                "prenom": prenom,
                "cin": client["cin"],
                "genre": client["genre"],
                "date_naissance": client["date_naissance"],
                "adresse": adresse,
                "telephone": telephone
            }
            clients.remove(client)
            clients.append(md_client)
            with open('client.json', 'w') as f:
                json.dump(file, f)
            break

# Fonction pour afficher les informations d'un client
def affiche_client():
    """
    Cette fonction permet d'afficher les information d'un client en donnant son cin
    """
    cin = input("Donner le cin de client que vous voulez afficher ses informations: ")
    for client in clients:
        if client["cin"] == cin:
            res = "\nnom: {} \nprenom: {} \ncin: {}\ngenre: {} \ndate_naissance: {} \nadresse: {} \ntelephone: {} \n"
            print(res.format(client["nom"], client["prenom"], client["cin"], client["genre"], client["date_naissance"],client["adresse"], client["telephone"]))

# Fonction pour afficher la liste des clients
def affichage_client():
    """
    Cette fonction permet d'afficher la liste des clients
    """
    for client in clients:
        res = "\nnom: {} \nprenom: {} \ncin: {}\ngenre: {} \ndate_naissance: {} \nadresse: {} \ntelephone: {} \n"
        print(res.format(client["nom"], client["prenom"], client["cin"], client["genre"], client["date_naissance"],
                         client["adresse"], client["telephone"]))

