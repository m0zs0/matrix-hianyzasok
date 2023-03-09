#0. feladat A hianyzasok.txt beolvasása listában listákba

hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf-8") as fm:
    for sor in fm:
        seged_lista=(sor.strip().split(","))
        # l=[]
        # for szam in seged_lista:
        #     l.append(int(szam))
        # hianyzasok.append(l)
        hianyzasok.append(list(map(int, seged_lista)))

print("a beolvasott mátrix: ")
print(hianyzasok)

<<<<<<< HEAD
# 1. Hány óra hiányzás volt összesen?
=======
>>>>>>> 2254e0cf4d5caf26a2f030c1bd611d1d316dd260
osszeg=0
for het in hianyzasok:
    osszeg+=sum(het)

<<<<<<< HEAD
=======
# 1. Hány óra hiányzás volt összesen?
>>>>>>> 2254e0cf4d5caf26a2f030c1bd611d1d316dd260
print(f"1. feladat: {osszeg} óra hiányzás volt összesen")