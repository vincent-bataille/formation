import os
import sys
import json

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "liste_course.json")

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

#si le fichier existe, je récupère son contenu dans liste
if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH,"r") as f:
        LISTE = json.load(f)
# sinon je créé liste à vide
else:
    LISTE =[]

# Je lance une boucle infinie
while True:
# j'initialize le choix du user
    user_choice = ""    
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")
    
    if user_choice == "1":  # Ajouter un élément
        item=input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"l'élément {item} a bien été ajouté")

    elif user_choice == "2":  # Retirer un élément
        item=input("Entrez le nom d'un élément à retirer la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"l'élément {item} a bien été retiré")
        else:
            print(f"l'élément {item} n'est pas dans la liste !")

    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("voici la liste :")
            for i, item in enumerate(LISTE,1):
                print(f"{i}. {item}")
        else:
            print("votre liste est vide")

    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste a été vidée")

    elif user_choice == "5":  # Quitter
        with open(LISTE_PATH,"w") as f:
            json.dump(LISTE, f, indent=4)
        print("A bientot !")
        sys.exit()

    print("-" * 50)
