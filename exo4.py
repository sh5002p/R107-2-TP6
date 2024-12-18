import random

nb = 100
def generer(vmin,vmax):
    nbr=[]
    for i in range(nb):
        nbr.append(random.randint(vmin,vmax))
    print(nbr)
    return nbr
def combienInferieur(nbr, vseuil, table = 0):
    for el in nbr:
        if el >= vseuil:
            table += 1
    return table

liste = generer(0,100)
resu = combienInferieur(liste,25)
print(resu)

print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
tab.sort()
print(tab)
total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")



