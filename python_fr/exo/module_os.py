## MODULE OS pour gérer les répertoires
# import de la fonction pprint du module pprint pour un affichage plus sympa
from pprint import pprint
# import du module OS
import os
# pour afficher toutes les fonctions du module (marche avec print mais c'est moins beau)
pprint(dir(os))
# pour afficher l'aide de la fonction walk
help(os.walk)
chemin = "/Users/vincentbataille/Desktop/formation/formation/python_fr/exo/"
dossier = os.path.join(chemin,"newfolder")
# création du dossier
if not os.path.exists(dossier):
    os.makedirs(dossier)
# suppression du dossier
if os.path.exists(dossier):
    os.removedirs(dossier)

