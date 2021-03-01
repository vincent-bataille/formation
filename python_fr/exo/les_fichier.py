chemin = "/Users/vincentbataille/Desktop/formation/formation/python_fr/exo/"
fichier = "fichier.txt"
file_to_open = chemin+fichier

# ouvrir en mode lecture

f=open(file_to_open, "r")
contenu = repr(f.read())
f.close()
print(contenu)

# ou mieux pour ne pas oublier le close :

with open(file_to_open, "r") as f:
    contenu = repr(f.read())
    print(contenu)

 # ou sous forme de liste :
with open(file_to_open, "r") as f:
    contenu = f.read().splitlines()
    print(contenu)
# pour info :
print("je\nsuis\nbeau".splitlines())

## Warning, après un read, le curseur est en fin de fichier
# pour remettre au début :
f.seek(0)

# ouvrir en w et écrire dans le fichier en ecrasant :
with open(file_to_open, "w") as f:
    f.write("bonjour")

# ouvrir en w et écrire dans le fichier en ajoutant :
with open(file_to_open, "a") as f:
    f.write("\nadios")
