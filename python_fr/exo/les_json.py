import json

chemin = "/Users/vincentbataille/Desktop/formation/formation/python_fr/exo/"
fichier = "test.json"
my_file = chemin+fichier

# écrire dans le json
with open(my_file,"w") as f:
    json.dump(list(range(10)),f,indent=4)

with open(my_file,"w") as f:
    json.dump("pêche",f,ensure_ascii=False)

# lire le json
with open(my_file,"r") as f:
    liste=json.load(f)
    print(liste)
