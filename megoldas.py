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
volt_e_otnel_kevesebb_hianyzas=False
for het in hianyzasok:
    if sum(het)<5:
        volt_e_otnel_kevesebb_hianyzas=True

if volt_e_otnel_kevesebb_hianyzas==True:
    print(f"3. feladat: Volt olyan hét, amikor ötnél kevesebb hiányzó volt")
else:
    print(f"3. feladat: Nem volt olyan hét, amikor ötnél kevesebb hiányzó volt")
