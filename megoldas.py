<<<<<<< HEAD
#0. feladat A hianyzasok.txt beolvasása listában listákba

hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf-8") as fm:
    for sor in fm:
        seged_lista=(sor.strip().split(","))
=======
#0. feladat A hianyzasok.txt beolvasásása listában listákba
#állománybeolvasás kész
hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf8") as fm:
    for sor in fm:
        seged_lista=sor.strip().split(",")
>>>>>>> 99f87eb99c4d1e2f59e710c929e166b3c3956e7d
        # l=[]
        # for szam in seged_lista:
        #     l.append(int(szam))
        # hianyzasok.append(l)
        hianyzasok.append(list(map(int, seged_lista)))

print(hianyzasok)