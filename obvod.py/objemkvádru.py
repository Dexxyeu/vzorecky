print("Vítejte v aplikaci pro výpočet objemu kvádru")

a = input("Zadejte stranu a : ")
b = input("Zadejte stranu b : ")
c = input("Zadejte stranu c :")

a = int(a)
b = int(b)
c = int(c)

if a>0 and b>0 and c>0:
    print("výsledek je : ")
    print(a*b)

else:
    print("copak to děláš? však si zadal záporné číslo")
