import json
import statistics
import matplotlib.pyplot as plt

with open('client.json', 'r') as f:
    file1 = json.load(f)
with open("bibliotheque.json") as f:
    file3=json.load(f)
with open('empreint.json', 'r') as f:
    file2 = json.load(f)

clients=file1["clients"]
empreints=file2["empreint"]
livres= file3["livres"]
magazines=file3["magazines"]
dvds=file3["dvds"]


def statistique():
    """
    Cette fonction permet de donner les statistiques en comptant le nombre de prêts pour chaque catégorie et pour chaque genre
    """
    stats = {}
    genre=[]
    for client in clients:
        genre = client['genre']
        for empreint in empreints:
            if empreint['cin de client'] == client['cin']:
                categorie = []
                res = empreint["entites"]  #La variable res reçoit la liste des empreint de client
                for livre in livres:  #Ensemble des boucles pour parcourir la bibliothèque
                    for magazine in magazines:
                        for dvd in dvds:
                            for i in res: #Boucle pour parcourir la liste de res, puis rechercher chaque entité dans la bibliothèque afin d'extraire sa catégorie
                                if i==livre["titre"] :
                                    categorie=livre["categorie"]
                                elif i==magazine["titre"]:
                                    categorie=magazine["categorie"]
                                elif i==dvd["titre"]    :
                                    categorie=dvd["categorie"]
                if genre not in stats:
                    stats[genre] = {}
                if categorie not in stats[genre]:
                    stats[genre][categorie] = 0
                stats[genre][categorie] += 1
    # Calculer les pourcentages des catégories empruntées pour chaque genre
    for genre, categories in stats.items():
        total = sum(categories.values())
        print(f"{genre} :")
        for categorie, nombre in categories.items():
            pourcentage = statistics.mean([nombre / total])
            print(f"\t{categorie} : {pourcentage * 100:.2f}%")
    return stats

def histogramme(stats):
    """
    Cette fonction permet de tracer les histogrammes correspondant aux résultats des statistiques
    """
    for genre, categories in stats.items():
        total = sum(categories.values())
        plt.bar(categories.keys(), [val / total for val in categories.values()])
        plt.title(f"Pourcentage des catégories empruntées par les {genre}")
        plt.show()

