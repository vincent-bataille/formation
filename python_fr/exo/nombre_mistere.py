from random import randint

n_to_find = randint (0,100)
n_attempts = 5

print("*** Le Jeu Du Nombre Mystère")

while n_attempts > 0:
    print(f"il vous reste {n_attempts} essai{'s' if n_attempts > 1}")
    u_in = input("devine le nombre : ")
    while not u_in.isdigit():
        print("veuillez entrer un nombre !")
        u_in = input("devine le nombre : ")
    u_in = int(u_in)
    if n_to_find == u_in:
        print(f"Well done ! c'était bien {u_in}")
        break
    elif n_to_find > u_in:
        print(f"le nombre mystère est plus grand que {u_in}")
        n_attempts -=1
        continue
    elif n_to_find < u_in:
        print(f"le nombre mystère est plus petit que {u_in}")
        n_attempts -=1
        continue
