# création d'une liste vide
liste=[]
# une liste peut contenir des types différents
liste=[250, "Python", True]
# note
# le mot "list" est réservé.

# ajout une valeur dans une liste :
liste.append(10.0)
print(liste)
# ajouter plusieurs valeurs sand une liste :
liste.extend([10,"le point",20])
print(liste)
# supprimer un élément de la liste
liste.remove(True)
print(liste)

# récupérer un élément de la liste :
élém = liste[2]
print(élém)

# Slices (tranches):
liste_users = ["u0","u1","u2","u3","u4"]
print(liste_users[0:2])
print(liste_users[0:5])
print(liste_users[0:5:2])

# récupérer l'index dans la liste
res = liste_users.index('u1')
print(res)

# compter le nombre d'occurence dans la liste
nbr_occ=liste_users.count('u1')
print(nbr_occ)

# trier la liste
liste_users.sort()
print(liste_users)
#ou pour envoyer dans une variable :
liste_trié=sorted(liste_users)
print(liste_trié)

# inverser une liste :
liste_a_inverser=["u10","a20","b16","v12"]
liste_a_inverser.reverse()
print(liste_a_inverser)

# retirer un élément de la liste par son index :
ma_liste=["u0","u1","u2","u3","u4"]
le_pop=ma_liste.pop(-1)
print(ma_liste)
print(le_pop)

# vider une liste
liste_a_vider=["u0","u1","u2","u3","u4"]
liste_a_vider.clear()
print(liste_a_vider)

# transformer une chaine de caractère en liste
courses = "Riz, Pomme, Lait, Salade, Saumon, Beurre"
courses = courses.split(", ")
print(courses)

# vérifier q'une occurence est dans la liste
#a faire avant un remove
courses=['Riz', 'Pomme', 'Lait', 'Salade', 'Saumon', 'Beurre']
if 'Riz' in courses:
    print(f"il y a 'riz' dans la liste")
#comparateur in :
test = 'jour' in 'bonjour'
print(test)

# listes imbriquées :
liste = ["e1",["e2-1","e2-2"]]
print(liste[1][1][2:])