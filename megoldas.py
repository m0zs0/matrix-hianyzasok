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

# 1. Hány óra hiányzás volt összesen?
osszeg=0
for het in hianyzasok:
    osszeg+=sum(het)

# 1. Hány óra hiányzás volt összesen?
print(f"1. feladat: {osszeg} óra hiányzás volt összesen")

# 3. Volt-e olyan hét, amikor ötnél kevesebb hiányzás volt
print("3. feladat:", end="")

for het in hianyzasok:
    if sum(het)<5:
        print(f" Volt olyan hét, amikor ötnél kevesebb hiányzó volt")
    else:
        print("Nem volt olyan hét, amikor ötnél kevesebb hiányzó volt")
