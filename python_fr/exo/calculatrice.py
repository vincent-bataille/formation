a = input ("entrez un premier nombre : ")
b = input ("entrez un deuxieme nombre : ")
while not a.isdigit() or not b.isdigit():
    print ("Veuillez entrer deux nombres valides")
    a = input ("entrez un premier nombre : ")
    b = input ("entrez un deuxieme nombre : ")
a = int(a)
b = int(b)
result = a+b
print(f"Le résultat de l'addition de {a} avec {b} est égal à {result}")
    