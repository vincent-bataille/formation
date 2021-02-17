# boucle for
liste=[1,12,3,4,5]
for i in liste:
    print(i)

for lettre in "python":
    print(lettre)

for i in range(10):
    print(i)

# boucle while
i=0
while i<10:
    print('bonjour')
    i +=1

continuer="o"
while continuer == 'o':
    print("On continue...")
    continuer=input("voulez vous continuer ? o/n : ")

import time

i=0
while i<2:
    print("sauvegarde en cours...")
    time.sleep(2)
    i+=1

# continue, permet de passer à la prochaine itération de suite
liste=["1","4","25","Paul","3","pierre"]
for element in liste:
    if element.isdigit():
        print('analyse...')
        continue
    print(element)

# break, fait sortir de la boucle
print("## le break")
liste=["1","4","25","Paul","3","pierre"]
for element in liste:
    if not element.isdigit():
        print('analyse...')
        break
    print(element)

# compréhension de liste
liste = [-4,-3,-2,-1,0,1,2,3,4]
nombres_positifs=[i*2 for i in liste if i>0]
print(nombres_positifs)