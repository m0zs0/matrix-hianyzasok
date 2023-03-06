#0. feladat A hianyzasok.txt beolvasásása listában listákba

hianyzasok=[]
with open("./adatok/hianyzasok.txt","r",encoding="utf8") as fm:
    for sor in fm:
        seged_lista=sor.strip().split(",")
        # l=[]
        # for szam in seged_lista:
        #     l.append(int(szam))
        # hianyzasok.append(l)
        hianyzasok.append(list(map(int, seged_lista)))

print(hianyzasok)