# On importe ici les modules et les fichiers python qu'on a implémentés
from client import *
from bibliotheque import *
from abonnement import *
from empreint import *
from historique import *
from blacklist import *
from notification import *
from recherche import *
from statistique import *


def gestion_client():
    """
    Cette fonction permet la gestion des clients de la bibliothèque
    """
    while True:
        ok = input("Voulez-vous ajouter un nouveau client? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        ajouter_client()
    while True:
        ok = input("Voulez-vous modifier les informations d'un client? (oui/non)\n")
        if ok == "oui" or ok=="non":
            break
    if ok == "oui":
        modifier_client()
    while True:
        ok = input("Voulez-vous supprimer un client? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        supprime_client()
    while True:
        ok = input("Voulez-vous afficher les information d'un client? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affiche_client()
    while True:
        ok = input("Voulez-vous ajouter un nouvel historique d'un client? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        ajout_hist()
    while True:
        ok = input("Voulez-vous afficher l'historique d'un client ? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affiche_hist()
    while True:
        ok = input("Voulez-vous afficher la liste complete des clients? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affichage_client()
    while True:
        ok = input("Voulez-vous afficher l'historique des tous les clients? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affichage_hist()


def gestion_bibliotheque():
    """
    Cette fonction permet la gestion des ressources de la bibliothèque
    """
    while True:
        ok = input("Voulez-vous ajouter une nouvelle entite a la bibliotheque? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        ajout_bib()
    while True:
        ok = input("Voulez-vous modifier une entite de la bibliotheque? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        modifier_bib()
    while True:
        ok = input("Voulez-vous supprimer une entite de la bibliotheque? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        supprime_bib()
    while True:
        ok = input("Voulez-vous afficher les informations d'une entite de la bibliotheque? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affiche_bib()
    while True:
        ok = input("Voulez-vous afficher toute la bibliothque? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affichage_tous_bib()
    while True:
        ok = input("Voulez-vous rechercher un titre dans la bibliotheque? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        exp = input("Donner alors une expression a chercher : ")
        resultat = recherche_titre(exp)
        for r in resultat:
            print(r["titre"])
    while True:
        ok = input("Voulez-vous voir si un titre est encore disponible dans la bibliotheque? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        exp = input("Donner alors un titre pour verifier sa disponabilite : ")
        resultat = disponible(exp)
        print(resultat)


def gestion_abonnement():
    """
    Cette fonction permet la gestion des abonnements des clients
    """
    while True:
        ok = input("Voulez-vous ajouter un nouvel abonnement? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        ajout_abn()
    while True:
        ok = input("Voulez-vous supprimer un abonnement? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        supprime_abn()
    while True:
        ok = input("Voulez-vous afficher les informations d'un abonnement? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affiche_abn()
    while True:
        ok = input("Voulez-vous afficher la liste des abonnements? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affichage_abn()


def gestion_emprunt():
    """
    Cette fonction permet la gestion des emprunts des clients de la bibliothèque
    """
    while True:
        ok = input("Voulez-vous ajouter un nouveau empreint? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        ajout_emp()
    while True:
        ok = input("Voulez-vous supprimer un emprunt? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        supprime_emp()
    while True:
        ok = input("Voulez-vous afficher les informations d'un emprunt? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affiche_emp()
    while True:
        ok = input("Voulez-vous afficher la liste des emprunts? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affichage_emp()

def gestion():
    """
    Cette fonction permet la gestion du Blacklist, les notifications, les rentrées/mois et les différents statistiques
    """
    ajout_bl()
    while True:
        ok = input("Voulez-vous afficher le contenu de Blackliste? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        affichage_bl()
    while True:
        ok = input("Voulez-vous voir les notifications? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        notification()
    while True:
        ok = input("Voulez-vous afficher les rentrees par mois? (oui/non)\n ")
        if ok =="oui" or ok == "non":
            break
    if ok == "oui":
        s = 0
        for abn in abnment:
            if abn["type"] == "normal":
                s += 15     #Pour un abonnement normal, le client doit payer 15Dt
            elif abn["type"] == "premium":
                s += 25     #Pour un abonnement premium, le client doit payer 25Dt
        print("Les rentrees par mois sont: ", s , "Dinars/mois")
    while True:
        ok = input("Voulez-vous afficher des statistiques? (oui/non)\n ")
        if ok == "oui" or ok == "non":
            break
    if ok == "oui":
        s=statistique()
        print("Voici les histogrammes modelisant les donnees des statistiques: ")
        histogramme(s)
